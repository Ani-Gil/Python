# 150.py - 디렉터리에 있는 파일목록 얻기(os.listdir, glob.glob)

import os, glob

folder = 'd:/devlab/py200'
file_list = os.listdir(folder)
print(file_list)

files = '*.txt'
file_list = glob.glob(files)
print(file_list)