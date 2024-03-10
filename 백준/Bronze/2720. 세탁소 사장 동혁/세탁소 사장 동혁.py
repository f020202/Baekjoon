iter = int(input())
for _ in range (iter):
    rest = int(input())
    a = b= c= d =0
    
    if rest > 0:
        a = rest//25
        rest = rest - a*25
    if rest > 0:
        b = rest // 10
        rest = rest - b * 10
    if rest > 0:
        c = rest // 5
        rest = rest - c * 5
    if rest > 0:
        d = rest // 1
        rest = rest - d * 1
        
    print(a,b,c,d)