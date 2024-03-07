T=int(input())
for i in range(0,T):
    S = input()
    S_list = S.split()
    S_num = int(S_list[0])
    S_str = list(S_list[1])

    result = list(map(lambda x: x * S_num, S_str))

    print(''.join(result))