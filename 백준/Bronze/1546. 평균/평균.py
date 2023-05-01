n = int(input())
a = input()
a= list(map(int, a.split()))
max = a[0]

for i in a:
    if i>max:
        max=i

sum = 0
for i in range(len(a)):
    a[i] = (a[i]/max) * 100
    sum += a[i]

print(sum/len(a))