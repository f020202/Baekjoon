T = int(input())
result = []
i = 2

while T>= i:
    if T%i == 0:
        result.append(i)
        T = T/i
    else:
        i+=1

print(*result, sep="\n")