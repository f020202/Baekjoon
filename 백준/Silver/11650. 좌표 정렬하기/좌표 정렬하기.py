import sys
input = sys.stdin.readline

n = int(input())
point = []
for _ in range(n):
    a,b = map(int,input().split())
    point.append([a,b])
point.sort()

for value in point:
    print(value[0],value[1])