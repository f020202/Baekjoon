def solution(phone_number):
    num = [int(x) for x in phone_number]
    for i in range(0,len(phone_number)-4):
        num[i] = "*"
    result = ''.join(map(str,num))
    return result
    
    