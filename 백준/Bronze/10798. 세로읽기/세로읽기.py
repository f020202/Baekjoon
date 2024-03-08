a = []
max_length = 0
for i in range(5):
    s = list(input())
    if len(s) > max_length:
        max_length = len(s)
    a.append(s)

for i in range(5):
    while len(a[i]) < max_length:
        a[i].append(".")

for i in range(max_length):
    for j in range(5):
        if a[j][i] != ".":
            print(a[j][i],end="")