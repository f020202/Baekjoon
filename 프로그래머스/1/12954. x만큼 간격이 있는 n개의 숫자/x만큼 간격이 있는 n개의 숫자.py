def solution(x, n):
    if x == 0:
        arr = [0]*n
    elif x*n > 0:
        arr = [x for x in range(x,x*n+1,x)]
    else:
        arr = [x for x in range(x,x*n-1,x)]
    return arr