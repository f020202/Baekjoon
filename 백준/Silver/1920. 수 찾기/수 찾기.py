n = int(input())
list1 = set(map(int,input().split()))
m = int(input())
list2 = list(map(int,input().split()))

for value in list2:
    if value in list1:
        print(1)
    else:
        print(0)