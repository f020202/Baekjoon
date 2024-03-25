n = int(input())
cnt = 0

while 1:
    list = [int(i) for i in str(cnt)]
    if n == cnt + sum(list):
        print(cnt)
        break
    cnt += 1
    if cnt >= 1000000:
        print(0)
        break