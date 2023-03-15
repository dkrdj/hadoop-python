import os
from pydub import AudioSegment
import shutil
import soundfile as sf
import librosa
from spleeter.separator import Separator

def separate_vocals(src_dir, dest_dir, num_stems=2):

    for root, dirs, files in os.walk(src_dir):
        print(root, dirs, files)
        new_root = root.replace(src_dir, dest_dir)

        if not os.path.exists(new_root):
            os.makedirs(new_root)

        for filename in files:
            new_wav_path = f'{new_root}/{filename[:-4]}.wav'
            if filename.endswith(".mp3") and not os.path.exists(new_wav_path):
                # 버퍼 문제가 있기 때문에 for문마다 실행해야 한다.
                separator = Separator(f"spleeter:{num_stems}stems")
                mp3_path = os.path.join(root, filename)
                wav_path = os.path.join(new_root, filename.replace(".mp3", ".wav"))
                
                # mp3_path에 있는 mp3 파일을 wav 파일로 변환하여 저장
                sound = AudioSegment.from_file(mp3_path, format="mp3")
                sound.export(wav_path, format="wav")

                # 가수 폴더 생성하고 목소리, 악기음 분리
                separator.separate_to_file(wav_path, new_root)
                print(filename)
                shutil.move(f'{new_root}/{filename[:-4]}/vocals.wav', new_wav_path)
                shutil.rmtree(f'{new_root}/{filename[:-4]}')

                y, sr = librosa.load(new_wav_path)
                y_trimmed, _ = librosa.effects.trim(y, top_db=10, frame_length=512, hop_length=64)
                sf.write(new_wav_path, y_trimmed, sr)


separate_vocals("C:/Users/SSAFY/Desktop/SSAFY/projects/PJT2/data/sample", "C:/Users/SSAFY/Desktop/SSAFY/projects/PJT2/data/output", 2)

# separate_vocals(input_folder_path, ouput_folder_path, 2)
#   input_folder_path : mp3 파일이 있는 루트 폴더
#   output_folder_path : wav 파일을 저장할 루트 폴더

#       [폴더구조]
#       - INPUT_FOLDER_PATH/
#           - 가수1/
#               - 1.mp3
#               - 2.mp3
#           - 가수2/
#               - 1.mp3
#               - 2.mp3
#           ...
#       - OUTPUT_FOLDER_PATH/
#           - 가수1/
#               - 1.wav
#               - 2.wav
#           - 가수2/
#               - 1.wav
#               - 2.wav
#           ...