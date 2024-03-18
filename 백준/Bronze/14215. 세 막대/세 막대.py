a = list(map(int,input().split()))
a.sort()
sum = a[0]+a[1]

# a[2]가 max값
if a[2] < sum:
    print(sum+a[2])
else:
    print(sum+sum-1)