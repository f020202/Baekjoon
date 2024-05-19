def solution(s, n):
    s = list(s)
    arr = []
    for char in s:
        char = ord(char)
        if char > 64 and char < 91:
            if char + n > 90:
                arr.append(n+char-26)
            else:
                arr.append(char+n)
        elif char > 96 and char < 123:
            if char + n > 122:
                arr.append(n-122+char+96)
            else:
                arr.append(char+n)
        elif char == 32:
            arr.append(32)
    arr = [chr(x) for x in arr]
    result = ''.join(arr)
    return result
            
        