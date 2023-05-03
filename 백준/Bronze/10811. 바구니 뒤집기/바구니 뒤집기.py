n, m = map(int, input().split())
list1 = []
for i in range(1,n+1):
    list1.append(i)

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a==0:
        list1[a:b+1] = list1[b::-1]
    else:
        list1[a:b+1] = list1[b:a-1:-1]

print(*list1)

# list1[1:5] = list1[4:0:-1] # 1번 인덱스 - 4번 인덱스
# list1[1:5] = list1[4::-1] # 0번 인덱스 - 4번 인덱스
# print(list1)