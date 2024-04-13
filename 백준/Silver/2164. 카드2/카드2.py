from collections import deque

n = int(input())
card = [x for x in range(n,0,-1)]
card = deque(card)

while len(card) > 1:
    card.pop()
    card.rotate(1)

print(*card)