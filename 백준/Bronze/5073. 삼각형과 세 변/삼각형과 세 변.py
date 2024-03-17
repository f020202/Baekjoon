while 1:
    a = list(map(int,input().split()))
    if a[0]==a[1]==a[2]==0:
        break
    else:
        if max(a) >= sum(a) - max(a):
            print("Invalid")
        else:
            if a[0] == a[1] == a[2]:
                print("Equilateral")
            elif a[0] == a[1] or a[1] == a[2] or a[2] == a[0]:
                print("Isosceles")
            else:
                print("Scalene")