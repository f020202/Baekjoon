n,m = map(int, input().split())
arr = set()
cnt = 0

for _ in range(n):
    arr.add(input())

for _ in range(m):
    if input() in arr:
        cnt += 1
        
print(cnt)
