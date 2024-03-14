a = int(input())
b = int(input())
prime_list = []

for i in range(a, b+1):
    cnt = 0

    for j in range(2,i):
        if i%j == 0:
            cnt += 1
    if cnt == 0:
        prime_list.append(i)

if 1 in prime_list:
    prime_list.remove(1)

if len(prime_list) != 0:
    print(sum(prime_list))
    print(prime_list[0])
else:
    print(-1)