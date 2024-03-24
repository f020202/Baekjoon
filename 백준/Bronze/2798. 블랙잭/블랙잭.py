n,m = map(int,input().split())
card = list(map(int,input().split()))
sum = []

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum.append(card[i]+card[j]+card[k])

result = []

for i in range(len(sum)):
    if sum[i] <= m:
        result.append(sum[i])

print(max(result))