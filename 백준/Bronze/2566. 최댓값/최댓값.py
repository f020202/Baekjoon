num = 9
a=[]
for _ in range(num):
    try:
        input_matrix = list(map(int,input().split()))
        a.append(input_matrix)
    except EOFError:
        break

max = a[0][0]
max_i = 0
max_j = 0

for i in range(num):
    for j in range(num):
        if a[i][j] > max:
            max = a[i][j]
            max_i = i
            max_j = j

print(a[max_i][max_j])
print(max_i+1, max_j+1)