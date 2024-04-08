import sys
input = sys.stdin.readline

T = int(input())
stack = []

for _ in range(T):
    i = list(map(int, input().split()))

    # 명령이 1인 경우
    if i[0] == 1:
        stack.append(i[1])

    # 명령이 2인 경우
    elif i[0] == 2:
        if len(stack) > 0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)

    # 명령이 3인 경우
    elif i[0] == 3:
        print(len(stack))

    # 명령이 4인 경우
    elif i[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    # 명령이 5인경우
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])