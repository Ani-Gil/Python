# 187.py - 웹서버 로그 처리하기 사용자별 서비스 용량 계산하기[4]

services = []

with open('access_log', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        ip = log[0]
        if servicebyte.isdigit():
            servicebyte = int(servicebyte)
        else:
            servicebyte = 0

        if ip not in services:
            services[ip] = servicebyte
        else:
            services[ip] += servicebyte

ret = sorted(services.items(), key=lambda x: x[1], reverse = True)

print('사용자IP - 서비스 용량')
for ip, b in ret:
    print('[%s] - [%d]' % (ip, b))