n,m = map(int,input().split())
card = list(map(int,input().split()))
sum_list = []

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum = card[i]+card[j]+card[k]
            if sum <= m:
                sum_list.append(sum)

print(max(sum_list))