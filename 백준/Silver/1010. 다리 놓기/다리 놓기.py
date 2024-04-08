import math

def C(n,r):
    a = math.factorial(n)
    b = math.factorial(n-r)
    c = math.factorial(r)
    return a // (b*c)

n = int(input())

for _ in range(n):
    W, E = map(int,input().split())
    print(C(E,W))