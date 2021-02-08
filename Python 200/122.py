# 122.py - 리스트 요소가 모두 참인지 확인하기(all, any)

listdata1 = [0, 1, 2, 3, 4]
listdata2 = [True, True, True]
listdata3 = ['', [], (), {}, None, False]
print(all(listdata1))   # False가 출력됨
print(any(listdata1))   # True가 출력됨
print(all(listdata2))   # True가 출력됨
print(any(listdata2))   # True가 출력됨
print(all(listdata3))   # False가 출력됨
print(any(listdata3))   # False가 출력됨