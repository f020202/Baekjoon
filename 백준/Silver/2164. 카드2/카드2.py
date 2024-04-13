from collections import deque

n = int(input())
# n부터 1까지 큐에 넣기
card = [x for x in range(n,0,-1)]
card = deque(card)

while len(card) > 1:
    # pop으로 맨뒤에 있는거 삭제하기
    # 큐로 만든 후에 pop한거기때문에 시간초과 안뜸
    card.pop()
    # 큐 오른쪽으로 한칸씩 이동
    card.rotate(1)

print(*card)