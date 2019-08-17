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
                array[j] = array[j] + 

getWays(n,c)