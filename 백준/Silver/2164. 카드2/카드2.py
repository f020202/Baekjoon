from collections import deque

n = int(input())
card = [x for x in range(1,n+1)]
card = deque(card)

while len(card) > 1:
    # 맨 앞에있는거 삭제
    card.popleft()
    # 왼쪽으로 옮김 (맨앞 원소는 맨뒤로감)
    card.rotate(-1)

print(*card)