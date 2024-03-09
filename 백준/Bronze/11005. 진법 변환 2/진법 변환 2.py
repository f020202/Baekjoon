a,b = map(int,input().split())
result = []

while a >= b:
    c = a % b
    a = a//b
    result.insert(0,c)
result.insert(0,a)

for i in result:
    if i>9:
        i = chr(i+55)
    print(i,end="")