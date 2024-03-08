a = [0 for i in range(26)]
b= list(map(str.upper, list(input())))
c= list(map(lambda x:ord(x)-65,b))
for i in range(0,len(c)):
    a[c[i]]+=1

# d는 있는 알파벳 갯수만 추린 배열
d=[]
for i in range(0,26):
    if(a[i]!=0):
        d.append(a[i])

max_num = max(d)
d.remove(max_num)

if max_num in d:
    print("?")
else:
    max_alpha = a.index(max(a))
    print(chr(max_alpha+65))