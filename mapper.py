import sys
from spleeter.separator import Separator
from pydub import AudioSegment

MUSIC = "/user/j8a603/music/"

# 입력 파일 경로
input_path = "/input"

# 출력 파일 경로
output_path = "/output"

# 보컬 분리를 위한 함수
def separate_vocals(mp3_path, dest_dir, num_stems=2):
    separator = Separator(f"spleeter:{num_stems}stems")

    wav_path = mp3_path.replace(".mp3", ".wav")
    print(mp3_path)
    sound = AudioSegment.from_file(mp3_path, format="mp3")
    sound.export(wav_path, format="wav")

    separator.separate_to_file(wav_path, dest_dir)

# 맵 함수
def mapper():
    for line in sys.stdin:
        mp3_path = line.strip()
        separate_vocals(MUSIC + mp3_path, output_path)