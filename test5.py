import os

file = open("example.txt", 'w', encoding='utf-8')
for foldername in os.listdir("../song"):
    for filename in os.listdir("../song/"+foldername):
        file.write(foldername+'/'+filename+'\n')
file.close()