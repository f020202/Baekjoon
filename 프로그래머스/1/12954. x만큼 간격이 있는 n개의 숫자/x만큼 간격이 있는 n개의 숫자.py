def solution(x, n):
    if x*n > 0:
        arr = [x for x in range(x,x*n+1,x)]
    elif x == 0:
        arr = [0]*n
    else:
        arr = [x for x in range(x,x*n-1,x)]
    return arr