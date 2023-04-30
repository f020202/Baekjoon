n = int(input())
string = input()
cnt_num = input()
list = string.split()
cnt = 0
for i in list:
    if str(i) == cnt_num:
        cnt += 1

print(cnt)