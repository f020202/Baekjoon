def solution(n):
    result = -1
    for i in range(1,n+1):
        if i*i == n:
            result = (i+1)**2
            break
    return result