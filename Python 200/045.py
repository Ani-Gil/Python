# 045.py - 파이썬 모듈 임포트 이해하기(import)[1]

import time                                # 파이썬 내장 모듈인 time을 임포트함
import mylib                               # 내가 작성한 mylib 모듈을 임포트함
import mypackage.mylib                     # mypackage에 있는 mylib 모듈을 임포트함

time.sleep(1)                              # time 모듈의 sleep 함수를 이용해 1초간 정지
mylib.add_txt('나는', '파이썬이다')         # mylib 모듈의 add_txt 함수를 호출
mypackage.mylib.reverse(1, 2, 3)           # mypackage.mylib 모듈의 reverse 함수 호출