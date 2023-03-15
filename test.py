import sys, os, shutil, subprocess
from pydub import AudioSegment
from spleeter.separator import Separator

from multiprocessing import freeze_support

new_path = os.path.join(os.getcwd(), 'ffmpeg')

# 기존 PATH 목록을 가져와서 리스트로 변환
path_list = os.environ["PATH"].split(os.pathsep)

# 새로운 디렉토리 경로를 PATH 목록에 추가
path_list.append(new_path)

# PATH 목록을 다시 문자열로 변환하여 환경 변수에 저장
os.environ["PATH"] = os.pathsep.join(path_list)
sys.path.append(new_path)
print(os.environ["PATH"])

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
    print("목소리와 악기음 분리 완료")
    # 목소리 파일을 지정한 경로로 이동 시키기
    shutil.move(f'{output_dir}/{file_name[:-4]}/vocals.wav', new_wav_path)
    print("파일 이동 완료")
    # 분리한 파일(목소리와 악기음) 삭제
    shutil.rmtree(f'{output_dir}/{file_name[:-4]}')
    
    # path = input_path.split('/')[0]
    # shutil.rmtree(input_path.split('/')[0])
    print("필요없는 파일 삭제 완료")

if __name__ == '__main__':
    freeze_support()
    separate_vocals("music/iu.mp3", "output", 2)