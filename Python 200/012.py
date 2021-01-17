# 012.py - for문 개념 배우기 (for~continue~break) [2]

scope = [1, 2, 3, 4, 5]
x = 0
for x in scope:
    print(x)
    if x < 3:
        continue
    else:
        break