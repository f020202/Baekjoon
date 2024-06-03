def solution(left, right):
    def divisors(n):
        cnt = 0
        for i in range(1,n+1):
            if n%i == 0:
                cnt +=1
        return cnt
    
    sum = 0
    for i in range(left,right+1):
        if divisors(i) % 2 ==0:
            sum += i
        else:
            sum -= i
    return sum
            
    
        