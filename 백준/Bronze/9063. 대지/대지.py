x = []
y = []
iter = int(input())

for _ in range(iter):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

w = max(x) - min(x)
h = max(y) - min(y)
print(w*h)