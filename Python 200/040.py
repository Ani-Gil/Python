# 040.py - 함수 인자 이해하기

def add_txt(t1, t2='파이썬'):
    print(t1+':'+t2)

add_txt('베스트')                       # '베스트 : 파이썬'이 출력됨
add_txt(t2='대한민국', t1='1등')        # '1등 : 대한민국'이 출력됨

def funcl(*args):
    print(args)

def func2(widh, height, **kwargs):
    print(kwargs)

funcl()                                 # 빈 튜플 ()이 출력됨
funcl(3, 5, 1, 5)                       # (3, 5, 1, 5)가 출력됨
func2(10, 20)                           # 빈 사전 {}이 출력됨
func2(10, 20, depth=50, color='blue')   # {'depth':50, 'color':'blue'} 이 출력되