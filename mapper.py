#!pip install pydub

import sys, os, shutil, subprocess #시스템 패키지
subprocess.run(["hdfs", "dfs", "-get","/user/j8a603/lib", "lib"], check=True)
sys.path.append(0, './lib/site-packages')

from pydub import AudioSegment
from spleeter.separator import Separator

def separate_vocals(input_path, output_dir, num_stems=2):
    # 음원 파일 이름(~.mp3)
    file_name = input_path.split('/')[-1]

    separator = Separator(f"spleeter:{num_stems}stems")

    # mp3 파일을 wav 파일로 변환하여 저장함
    wav_path = input_path.replace(".mp3", ".wav")
    sound = AudioSegment.from_file(input_path, format="mp3")
    sound.export(wav_path, format="wav")
    print("wav로 파일 변환 완료")
    # 가수 이름
    singer = file_name.split('-')[0].strip()

    # 결과를 저장할 가수 폴더 경로
    new_root = os.path.join(output_dir, singer)
    # 보컬 파일 이름
    new_wav_path = f'{new_root}/{file_name[:-4]}.wav'

    # 가수 폴더 없다면 생성
    if not os.path.exists(new_root):
        os.makedirs(new_root)
        print("가수 폴더 생성 완료")

    # 목소리와 악기음 분리
    separator.separate_to_file(wav_path, output_dir)
    # 목소리 파일을 지정한 경로로 이동 시키기
    shutil.move(f'{output_dir}/{file_name[:-4]}/vocals.wav', new_wav_path)
    # 분리한 파일(목소리와 악기음) 삭제
    shutil.rmtree(f'{output_dir}/{file_name[:-4]}')
    
    path = input_path.split('/')[0]
    shutil.rmtree(input_path.split('/')[0])


input_dir = 'local_input'
output_dir = 'local_output'

for line in sys.stdin:
    
    input_path = os.path.join(input_dir, line).strip()
    
    hdfs_path = os.path.join('/user/j8a603/music', line).strip()

    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
    subprocess.run(["rm", "-r", input_dir], check=True)
    os.makedirs(input_dir)
    subprocess.run(["hdfs", "dfs", "-copyToLocal", hdfs_path, input_dir+'/'], check=True)
    separate_vocals(input_path, output_dir)
    subprocess.run(["hdfs", "dfs", "-put", output_dir, "music_output/"], check=True)