a,b = input().split()
c = int(input())
a= int(a)
b= int(b)

if b+c < 60:
    print(a, b+c)
else:
    min_sum = b+c
    hour = int(min_sum / 60)
    min = min_sum - hour*60
    if a+hour>23:
        print((a+hour)-24, min)
    else:
        print(a+hour, min)
