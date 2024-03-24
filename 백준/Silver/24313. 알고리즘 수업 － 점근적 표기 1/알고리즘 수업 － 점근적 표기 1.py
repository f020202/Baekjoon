a, b = map(int, input().split())
c = int(input())
n = int(input())

def f(x):
    return a * x + b

def cg(x):
    return c * x

if a>c:
    print(0)
elif a==c:
    if b<=0:
        print(1)
    else:
        print(0)
elif a<c:
    if cg(n) >= f(n):
        print(1)
    else:
        print(0)