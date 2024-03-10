iter = int(input())
coin = [25, 10, 5, 1]

for _ in range(iter):
    rest = int(input())
    for i in coin:
        a = rest // i
        if rest > 0:
            rest = rest - a * i
        print(a, end=" ")
    print("")