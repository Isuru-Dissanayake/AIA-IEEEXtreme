t = int(input())
for cases in range(t):
    n = int(input())
    paint = list(map(int,input().split()))
    br1 = []
    br2 = []
    paintSort = list(dict.fromkeys(paint))
    paintCount = [0 for i in range(len(paintSort))]
    for i in range(len(paint)):
        paintCount[paintSort.index(paint[i])] += 1
    
        