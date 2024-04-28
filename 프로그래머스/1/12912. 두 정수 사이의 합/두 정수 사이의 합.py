def solution(a, b):
    if b<a:
        a, b = b,a
    sum = 0
    for i in range(a,b+1):
        sum += i
    return sum