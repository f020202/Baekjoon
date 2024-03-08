n, m = map(int, input().split())
a = []
b = []

for _ in range(n):
    input_row = list(map(int, input().split()))
    a.append(input_row)

for _ in range(n):
    input_row = list(map(int, input().split()))
    b.append(input_row)

for i in range(n):
    for j in range(m):
        a[i][j] = a[i][j] + b[i][j]
        print(a[i][j], end=" ")
    print("")