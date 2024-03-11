T = int(input())
a = 2
b = 7
six = 1
answer = 0

while not (b >= T >= a) and T!=1:
    answer = (b-a+1)/6
    a+= 6*six
    b+= 6*(six+1)
    six += 1

if T == 1:
    print(1)
else:
    print(int(answer) + 2)
