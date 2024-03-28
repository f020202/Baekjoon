n = input()
num = list(map(int,n))

num.sort()
num.reverse()
print(*num, sep="")