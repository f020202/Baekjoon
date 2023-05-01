max = 0
max_num = 1
for i in range(1,10):
    n = int(input())
    if n>max:
        max = n
        max_num=i
print(max)
print(max_num)