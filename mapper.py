import sys
import os

# 파일 경로
path = sys.argv[1]

# 파일 목록 가져오기
files = os.listdir(path)

# 파일 처리
for file in files:
    # 파일 확장자가 mp3인 경우에만 처리
    if file.endswith(".mp3"):
        # 파일을 읽어서 처리
        with open(os.path.join(path, file), 'r') as f:
            for line in f:
                # separate_vocals(line) 함수 호출
                print(line)