def solution(A,B):
    sum = 0
    sorted_A = sorted(A)
    sorted_B = sorted(B,reverse=True)
    for a,b in zip(sorted_A,sorted_B):
        sum += a*b
    return sum 