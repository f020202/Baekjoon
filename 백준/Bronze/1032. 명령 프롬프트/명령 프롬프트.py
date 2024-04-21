n = int(input())
str = list(input())

for _ in range(n-1):
    str2 = list(input())
    for i in range(len(str)):
        if str[i] == str2[i]:
            continue
        else:
            str[i] = "?"

print(*str, sep="")