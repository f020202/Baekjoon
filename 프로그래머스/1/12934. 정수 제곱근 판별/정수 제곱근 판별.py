def solution(n):
    result = 0
    for i in range(1,n+1):
        if i*i == n:
            result = (i+1)**2
            break
    if result == 0:
        return -1
    else:
        return result