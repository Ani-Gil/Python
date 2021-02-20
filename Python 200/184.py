# 184.py - 웹서버 로그 처리하기 총 페이즈뷰 수 계산하기[1]

pageviews = 0

with open('access_log' 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        status = log[8]
        if status == '200':
            pageviews += 1

print('총 페이지뷰: [%d]' % pageviews)