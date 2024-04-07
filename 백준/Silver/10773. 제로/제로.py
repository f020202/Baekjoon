n = int(input())
cnt = []
for _ in range(n):
    num = int(input())
    if num != 0:
        cnt.append(num)
    else:
        cnt.pop()
        
print(sum(cnt))

        