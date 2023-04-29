cost = int(input())
n = int(input())
sum = 0

for i in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    sum += a*b

if cost == sum:
    print("Yes")
else:
    print("No")
