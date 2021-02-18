# 173.py - 인터넷에 있는 대용량 파일을 내 PC로 저장하기

from urllib.request import urlopen

BUFSIZE = 256 * 1024

fileurl = 'https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe'
filename = fileurl.split('/')[-1]
try:
    with urlopen(fileurl) as f:
        with open(filename, 'wb') as h:
            buf = f.read(BUFSIZE)
            while buf:
                h.write(buf)
                buf = f.read(BUFSIZE)
except Exception as e:
    print(e)