n = int(input())
cnt = 0

while 1:
    # cnt 쪼개서 list에 넣기
    list = [int(i) for i in str(cnt)]
    # n = 198 + (1+9+8) 이 되면 멈추기
    if n == cnt + sum(list):
        print(cnt)
        break
    # cnt 값 하나 올리기
    cnt += 1
    # 만약 cnt가 1000000을 넘어가면 생성자가 없음
    if cnt >= 1000000:
        print(0)
        break