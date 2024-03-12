while 1:
    T = int(input())
    list = []

    if T == -1:
        break
    else:
        for i in range(1,T):
            if T%i ==0:
                list.append(i)

        if sum(list) == T:
            print(T, end=" = ")
            for i in range(len(list)):
                if i == len(list) -1:
                    print(list[i])
                else:
                    print(list[i], end=" + ")
        else:
            print(f"{T} is NOT perfect.")