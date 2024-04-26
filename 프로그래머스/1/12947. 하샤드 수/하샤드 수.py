def solution(x):
    arr = [int(x) for x in str(x)]
    if x % sum(arr) == 0:
        return True
    else:
        return False