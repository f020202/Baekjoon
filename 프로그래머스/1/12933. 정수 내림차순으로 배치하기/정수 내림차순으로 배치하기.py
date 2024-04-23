def solution(n):
    num = list(map(int,str(n)))
    num.sort(reverse = True)
    result = ''.join(map(str,num))
    return int(result)