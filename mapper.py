#encoding : utf-8

from io import BytesIO
from pydub import AudioSegment
from hdfs import InsecureClient
import os
import spleeter
import sys

def separate_vocals(mp3_data):
    

    # BytesIO 객체에 mp3 데이터를 쓴 후, AudioSegment 객체로 변환합니다.
    mp3_audio = AudioSegment.from_file(BytesIO(mp3_data), format="mp3")
    
    # AudioSegment 객체를 wav 데이터로 변환합니다.
    wav_data = mp3_audio.export(format="wav").read()

    # spleeter를 사용하여 보컬을 분리합니다.
    separator = spleeter.Separator(f"spleeter:2stems")
    waveform, _ = spleeter.io.load_wav_from_buffer(wav_data)
    prediction = separator.separate(waveform)
    

for line in sys.stdin:
    print(line)
    # separate_vocals(line)