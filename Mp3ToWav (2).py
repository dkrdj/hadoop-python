## 라이브러리 설치 필요
# !pip install pydub spleeter

import os
from pydub import AudioSegment
import shutil
import soundfile as sf
import librosa
from spleeter.separator import Separator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import librosa.display
import IPython.display as ipd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
                

def separate_vocals(mp3_path, dest_dir, num_stems=2):

    separator = Separator(f"spleeter:{num_stems}stems")

    wav_path = mp3_path.replace(".mp3", ".wav")
    sound = AudioSegment.from_file(mp3_path, format="mp3")
    sound.export(wav_path, format="wav")

    separator.separate_to_file(wav_path, dest_dir)
                

# separate_vocals(mp3_path, ouput_folder_path, 2)
#   mp3_path : mp3 파일 경로
#   output_folder_path : wav 파일을 저장할 폴더 경로
separate_vocals("/content/drive/MyDrive/TONEMATE/test/태연/태연 - 1111.mp3", "/content/drive/MyDrive/TONEMATE/sample", 2)