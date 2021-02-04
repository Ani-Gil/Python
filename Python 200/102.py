# 102.py - 리스트에서 특정 위치의 요소를 변경하기

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천완성', '해왕성']
planet = '화성'
pos = solarsys.index(planet)
solarsys[pos] = 'Mars'
print(solarsys)