# 046.py - 파이썬 모듈 임포트 이해하기(import)[2]

from time import sleep
from mypackage import mylib
from mypackage.mylib import reverse

sleep(1)                                # time 모듈의 sleep 함수 호출
mylib.add_txt('나는', '파이썬이다')      # mypackage.mylib 모듈의 add_txt 함수 호출
reverse(1, 2, 3)                        # mypackage.mylib 모듈의 reverse 함수 호출
