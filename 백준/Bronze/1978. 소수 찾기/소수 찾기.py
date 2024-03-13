T = int(input())
list1 = list(map(int, input().split()))
cnt = 0

for i in range(len(list1)):
    if list1[i] != 1:
        sum = 0

        for j in range(2, list1[i]):
            if list1[i] % j == 0:
                sum -= 1

        if sum == 0:
            cnt += 1
print(cnt)