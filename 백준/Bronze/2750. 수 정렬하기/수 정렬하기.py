n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

num.sort()
print(*num, sep="\n")