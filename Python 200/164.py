# 164.py - URL에서 쿼리 문자열 추출하기
url = 'http:/news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=028&aid=0002334601'

tmp = url.split('?')
queries = tmp[1].split('&')
for query in queries:
    print(query)