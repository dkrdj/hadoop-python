import os, sys

new_path = os.path.join(os.getcwd(), 'ffmpeg')

# 기존 PATH 목록을 가져와서 리스트로 변환
path_list = os.environ["PATH"].split(os.pathsep)

# 새로운 디렉토리 경로를 PATH 목록에 추가
path_list.append(new_path)

# PATH 목록을 다시 문자열로 변환하여 환경 변수에 저장
os.environ["PATH"] = os.pathsep.join(path_list)
sys.path.append(new_path)

def which(program):
    """
    Mimics behavior of UNIX which command.
    """
    # Add .exe program extension for windows support
    if os.name == "nt" and not program.endswith(".exe"):
        program += ".exe"
    envdir_list = [os.curdir] + os.environ["PATH"].split(os.pathsep)
    for envdir in envdir_list:
        program_path = os.path.join(envdir, program)
        if os.path.isfile(program_path) and os.access(program_path, os.X_OK):
            return program_path
        
print(which('ffmpeg'))