def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            result = f"김서방은 {i}에 있다"
            break
    return result