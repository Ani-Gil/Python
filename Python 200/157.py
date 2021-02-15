# 157.py - 현재 시간을 년-월-일 시:분:초로 출력하기(localtime, strftime)

from time import localtime, strftime

logfile = 'test.log'
def writelog(logfile, log):
    time_stamp = strftime('%Y-%m-%d %X\t', localtime())
    log = time_stamp + log + '\n'

    with open(logfile, 'a') as f:
        f.writelines(log)

writelog(logfile, '첫 번쨰 로깅 문장입니다.')