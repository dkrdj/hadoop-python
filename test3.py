import sys, os

new_path = os.getcwd()
new_path = os.path.join(new_path, 'ffmpeg-python')

# 기존 PATH 목록을 가져와서 리스트로 변환
path_list = os.environ["PATH"].split(os.pathsep)

# 새로운 디렉토리 경로를 PATH 목록에 추가
path_list.append(new_path)

# PATH 목록을 다시 문자열로 변환하여 환경 변수에 저장
os.environ["PATH"] = os.pathsep.join(path_list)

for envdir in os.environ["PATH"].split(os.pathsep):
    print(envdir)