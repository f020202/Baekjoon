a,b = map(int,input().split())
score = list(map(int,input().split()))
price = []

for _ in range(b):
    price.append(max(score))
    score.remove(max(score))

print(price[-1])