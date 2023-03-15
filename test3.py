import sys, os

sys.path.append('C:/Users/SSAFY/Desktop/hadoop-python/here')
for envdir in os.environ["PATH"].split(os.pathsep):
    print(envdir)