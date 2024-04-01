n = int(input())
arr1 = set(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

for value in arr2:
    if value in arr1:
        print(1, end=" ")
    else:
        print(0, end=" ")

# arr2의 원소가 arr1에 있는지 찾는것
# arr1을 돌아야함... => arr1이 set이면 된다??