a,b,c = map(int,input().split())

left = c-a
up = a-b

if a == c:
    result = 1
else:
    if left % up == 0:
        if left // up > 0:
            result = left // up + 1
        else:
            result = 2
    else:
        result = left // up + 2

print(result)