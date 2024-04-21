def solution(s):
    result = False
    s = list(s)
    p_num = 0
    y_num = 0
    for i in range(len(s)):
        if s[i] == "p" or s[i] == "P":
            p_num += 1
        elif s[i] == "y" or s[i] == "Y":
            y_num += 1
    if p_num == y_num:
        result = True

    return result