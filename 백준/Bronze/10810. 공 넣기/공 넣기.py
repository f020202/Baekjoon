N, M  = map(int, input().split())
list = []
for i in range(N):
    list.append(0)

for i in range(M):
    a,b,c = map(int, input().split())
    for i in range(a,b+1):
        list[i-1]=c
        
print(*list)