t = int(input())
for cases in range(t):
    n = int(input())
    paint = list(map(int,input().split()))
    br1 = [0,paint[0]]
    br2 = [0]
    for i in range(1,len(paint)):
        p = paint[i]
        if (br1[-1] == p) or (br2[-1] == p):
            pass
        else:
            paintCheck = paint[i+1:]
            brInd1 = len(paint) + 1
            brInd2 = len(paint) + 1
            if br1[-1] in paintCheck:
                brInd1 = paintCheck.index(br1[-1]) 
            if br2[-1] in paintCheck:
                brInd2 = paintCheck.index(br2[-1]) 
            if brInd2 != (len(paint) + 1) and brInd2 != (len(paint) + 1):
                if brInd1 > brInd2:
                    br1.append(p)
                else:
                    br2.append(p)
            else:
                br2.append(p)
    print (len(br1) + len(br2) - 2)

        