# 119.py - 리스트 요소 무작위로 섞기(shuffle)

from random import shuffle

listdata = list(range(1, 11))
for i in range(3):
    shuffle(listdata)
    print(listdata)     # 출력 결과는 실행할 때마다 달라짐%%%