T = int(input())
person = set()

for _ in range(T):
    a,b = input().split()
    if b == 'enter':
        person.add(a)
    else:
        # set일 경우: discord
        # list의 경우: remove
        person.discard(a)

result = list(person)
result.sort(reverse=True)
print(*result, sep='\n')