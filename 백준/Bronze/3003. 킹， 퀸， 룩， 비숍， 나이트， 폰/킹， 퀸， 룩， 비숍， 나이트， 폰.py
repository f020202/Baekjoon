a=list(map(int,input().split()))
b=[1, 1, 2, 2, 2, 8]
c = [y - x for x, y in zip(a, b)]
c = list(map(str,c))
print(' '.join(c))