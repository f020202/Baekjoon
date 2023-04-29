a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a==b and b==c:
    print(10000+a*1000)
elif a==b and b!=c:
    print(1000 + a*100)
elif a!=b and b==c:
    print(1000 + b*100)
elif a==c and b!=c:
    print(1000 + a * 100)
elif a!=b and b!=c and c!=a:
    if a>b:
        if a>c:
            max=a
        elif a<c:
            max=c
    elif a<b:
        if b>c:
            max=b
        elif b<c:
            max=c
    print(max*100)

