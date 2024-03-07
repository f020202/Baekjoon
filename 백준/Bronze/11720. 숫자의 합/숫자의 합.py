a = int(input())
number = input()
b = list(map(int, str(number)))
sum = 0

for i in range (0,a):
    sum += b[i]

print(sum)