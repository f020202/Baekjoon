T = int(input())
init = 2

for _ in range(T):
    tmp = (2*init-1)**2
    init = 2*init -1

print(tmp)