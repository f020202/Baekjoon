num_list = input().split()
for i in range(0,2):
    num_list[i] = int(str(num_list[i])[::-1])

if(num_list[0]>num_list[1]):
    print(num_list[0])
else:
    print(num_list[1])