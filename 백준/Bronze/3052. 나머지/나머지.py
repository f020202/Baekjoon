list1 = []
list2 = []
for i in range(10):
    n = int(input())
    list1.append(n % 42)

for i in list1:
    if i not in list2:
        list2.append(i)

print(len(list2))