a = list(map(ord,input()))

for idx, val in enumerate(a):
    if 64 < val < 68:
        a[idx] = 3
    elif 67 < val < 71:
        a[idx] = 4
    elif 70 < val < 74:
        a[idx] = 5
    elif 73 < val < 77:
        a[idx] = 6
    elif 76 < val < 80:
        a[idx] = 7
    elif 79 < val < 84:
        a[idx] = 8
    elif 83 < val < 87:
        a[idx] = 9
    elif 86 < val < 91:
        a[idx] = 10

print(sum(a))