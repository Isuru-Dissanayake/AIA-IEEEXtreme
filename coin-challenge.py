#https://www.hackerrank.com/challenges/coin-change/problem?isFullScreen=false

def getWays(n,c):
    array = [0]*(n+1)
    array[0] = 1
    for i in range(len(c)):
        for j in range(len(array)):
            ind = j - c[i]
            if ind < 0:
                pass
            else:
                array[j] = array[j] + array[ind]
        print (array)
    return(array[n])

n = int(input(""))
c = list(map(int,(input("")).split()))

#n = 4
#c = [1,2,3]

print(getWays(n,c))
