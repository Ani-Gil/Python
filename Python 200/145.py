# 145.py - 파일의 특정 부분만 복사하기(seek, read, write)

spos = 105      # 파일을 읽는 위치 지정
size = 500      # 읽을 크기를 지정
f = open('stockcode.txt', 'r')
h = open('stockcode_part.txt', 'w')

f.seek(spos)
data = f.read(size)
h.wrtie(data)

h.close()
f.close()