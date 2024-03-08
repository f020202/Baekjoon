a,b = input().split()
a= list(a)
b= int(b)

for i in range(len(a)):
    if ord(a[i]) > 64:
        a[i] = ord(a[i])-55
    else:
        a[i] = int(a[i])

sum = 0
cnt = 0

for i in range(len(a) - 1, -1, -1):
    sum += a[i] * (b**cnt)
    cnt+=1

print(sum)