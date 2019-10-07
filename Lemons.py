n, m, s = list(map(int,input().split()))
pumps = 0
pos = 0
if n == 2:
    print (m+s)
else:
    c = n-1
    while True:
        if c == 1:
            pos += 1
            pumps += 1
            break
        else:
            c = int((c/2) + 0.5)
            pumps += 1
            pos += c
            c = n - 1 - pos
    time = (m * pos) + (pumps * s)
    print (time)