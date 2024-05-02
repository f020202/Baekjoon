def solution(arr, divisor):
    result = []
    for value in arr:
        if value % divisor == 0:
            result.append(value)
    result.sort()
    if len(result) == 0:
        result = [-1]
    return result