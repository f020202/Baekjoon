from itertools import *
def solution(number):
    cnt = 0
    case = list(combinations(number,3))
    for i in range(len(case)):
        if sum(case[i]) == 0:
            cnt+=1
    return cnt
        
    
    