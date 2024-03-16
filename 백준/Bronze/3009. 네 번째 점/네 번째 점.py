x=[]
y=[]

for _ in range(3):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

x1 = x[0]
x.remove(x1)
y1 = y[0]
y.remove(y1)

if x1 in x:
    x.remove(x1)
    print(x[0], end=" ")
else:
    print(x1, end=" ")

if y1 in y:
    y.remove(y1)
    print(y[0])
else:
    print(y1)
