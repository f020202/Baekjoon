def solution(a, b):
    if b<a:
        tmp = a
        a = b
        b = tmp
    sum = 0
    for i in range(a,b+1):
        sum += i
    return sum