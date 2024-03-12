a, b = map(int, input().split())
cnt = 0
list = []

for i in range(1,a+1):
    if a%i == 0:
        list.append(i)

if b > len(list):
    print(0)
else:
    print(list[b-1])