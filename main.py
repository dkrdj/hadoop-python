import subprocess

# Hadoop streaming jar 경로
HADOOP_STREAMING_JAR_PATH = "/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar"

# Spleeter 라이브러리 경로
SPLEETER_LIB_PATH = "/home/j8a603/.local/lib/python3.8/site-packages/spleeter"

PYDUB_LIB_PATH = "/home/j8a603/.local/lib/python3.8/site-packages/pydub"

INPUT_PREFIX = "hdfs://ip-172-26-0-222.ap-northeast-2.compute.internal:9000/user/j8a603"


# 입력 파일 경로
input_path = "/input"

# 출력 파일 경로
output_path = "/output"

# 보컬 분리를 위한 함수
if __name__ == "__main__":
    # 입력 파일 경로 설정
    input_uri = INPUT_PREFIX + input_path

    # 출력 파일 경로 설정
    output_uri = INPUT_PREFIX + output_path

    # 맵리듀스 명령어
    cmd = f"hadoop jar {HADOOP_STREAMING_JAR_PATH} \
        -files {SPLEETER_LIB_PATH} \
        -files {PYDUB_LIB_PATH} \
        -input {input_uri} \
        -output {output_uri} \
        -mapper 'python3 mapper.py' \
        -reducer 'python3 reducer.py'"
    

    # 명령어 실행
    subprocess.call(cmd, shell=True)


    import sys
from spleeter.separator import Separator
from pydub import AudioSegment
import hdfs


# 입력 파일 경로
input_path = "/user/j8a603/input"

# 출력 파일 경로
output_path = "/user/j8a603/output"

MUSIC = "/user/j8a603/music/"

# 보컬 분리를 위한 함수
def separate_vocals(mp3_path, dest_dir, num_stems=2):
    separator = Separator(f"spleeter:{num_stems}stems")

    wav_path = mp3_path.replace(".mp3", ".wav")
    sound = AudioSegment.from_file(mp3_path, format="mp3")
    sound.export(wav_path, format="wav")

    separator.separate_to_file(wav_path, dest_dir)

# 맵 함수
def mapper():
    for line in sys.stdin:
        mp3_path = line.strip()
        separate_vocals(MUSIC + mp3_path, output_path)
mapper()