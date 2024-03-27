T = int(input())
num = 666
cnt = 0

while 1:
    s = str(num)
    if '666' in s:
        cnt += 1

    if cnt == T:
        print(num)
        break

    num += 1