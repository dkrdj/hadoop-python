from io import BytesIO
from pydub import AudioSegment
from hdfs import InsecureClient
import os
import spleeter
import sys

def separate_vocals(file_name):
    hdfs_client = InsecureClient('hdfs://ip-172-26-0-222.ap-northeast-2.compute.internal:9000', user='j8a603')
    with hdfs_client.read('/user/j8a603/music/'+file_name) as reader:
        mp3_data = reader.read()

    # BytesIO 객체에 mp3 데이터를 쓴 후, AudioSegment 객체로 변환합니다.
    mp3_audio = AudioSegment.from_file(BytesIO(mp3_data), format="mp3")
    
    # AudioSegment 객체를 wav 데이터로 변환합니다.
    wav_data = mp3_audio.export(format="wav").read()

    # spleeter를 사용하여 보컬을 분리합니다.
    separator = spleeter.Separator('spleeter:2stems')
    waveform, _ = spleeter.io.load_wav_from_buffer(wav_data)
    prediction = separator.separate(waveform)
    
    # 분리된 보컬 파일을 저장합니다.
    for i, stem in enumerate(prediction):
        with hdfs_client.write('/user/j8a603/output/'+os.path.splitext(file_name)[0]+'_vocals{}.wav'.format(i+1)) as writer:
            spleeter.io.save_wav(stem, writer)

for line in sys.stdin:
    separate_vocals(line)