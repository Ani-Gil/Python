# 127.py - 사전에서 키만 추출하기(keys)

names = {'Mary' : 10999, 'Sams' : 2111, 'Aimy' : 9778, 'Tom' : 20245,
        'Michale' : 27115, 'Bob' : 5887, 'Kelly' : 7855}
ks = names.keys()
print(ks)

for k in ks:
    print('Key:%s \tValue:%d' % (k, names[k]))