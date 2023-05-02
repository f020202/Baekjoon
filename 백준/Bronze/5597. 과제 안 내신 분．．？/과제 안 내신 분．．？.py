list1 = []
list2 = range(1,31)

for i in range(28):
    n = int(input())
    list1.append(n)

list1.sort()

for i in list2:
    if i not in list1:
        print(i)