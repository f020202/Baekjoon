import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr1 = set(map(int, input().split()))
arr2 = set(map(int, input().split()))

cnt1 = 0
cnt2 = 0

for value in arr1:
    if value not in arr2:
        cnt1 += 1

for value in arr2:
    if value not in arr1:
        cnt2 += 1

print(cnt1+cnt2)
