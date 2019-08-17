#https://www.hackerrank.com/challenges/coin-change/problem?isFullScreen=false

n = 4
c = [1,2,3]

def getWays(n,c):
    array = [0]*len(c)
    array[0] = 1
    for i in range(len(c)):
        for j in range(len(array)):
            ind = j - c[i]
            if ind < 0:
                pass
            else:
                array[j] = array[j] + array[ind]
        print (array)
    return(array[len(c) - 1])

print(getWays(n,c))
