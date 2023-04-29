a,b = input().split()
a= int(a)
b= int(b)

if b-45>0 or b-45==0:
    print(a, b-45)
else:
    if a-1>0 or a-1==0:
        print(a - 1, 60 - (45 - b))
    else:
        print("23", 60 - (45 - b))