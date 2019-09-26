#https://csacademy.com/ieeextreme-practice/task/979a09a0cd8c4e98dd0a690f39a55bd2/

def find_loop(edges):
    loop = 0
    oddVer = 0
    for i in range(len(edges)):
        if len(edges[i])%2 == 1:
            oddVer += 1
    if  oddVer%2 == 0:
        loop = 1
    else:
        loop = 0
    #print (oddVer)
    return(loop)
def check_for_ones(edges):
    ones = []
    for i in range(len(edges)):
        if len(edges[i]) < 2:
            ones.append(i)
    if len(ones) == 0:
        onesAvailable = False
    else:
        onesAvailable = True
    return (ones, onesAvailable)
def remove_ones(edges):
    ones, onesAvailable = check_for_ones(edges)
    if onesAvailable:
        newEdges = []
        for i in range(len(edges)):
            if len(edges[i]) == 0:
                pass
            else:
                vertex = []
                for j in range(len(edges[i])):
                    if (edges[i][j] in ones):
                        pass
                    else:
                        vertex.append(edges[i][j])
                if (len(vertex) > 0):
                    newEdges.append(vertex)
        return(remove_ones(newEdges))  
    else:
        return (edges)

    
testCases = int(input(""))
for cases in range(testCases):
    loop = 0
    nm = list(map(int,(input("")).split()))
    e = list(map(int,(input("")).split()))
    edges = [[] for i in range(nm[0])]
    for i in range(len(e)):
        if i%2 == 0:
            edges[e[i]].append(e[i+1])
        elif i%2 == 1:
            edges[e[i]].append(e[i-1])
    if (nm[0] < 3 or nm[1] < 3):
        loop = 0
    else:
        edges = remove_ones(edges)
        #print (edges)
        if (len(edges) == 0):
            loop = 0
        else:
            loop = find_loop(edges)
    print (loop)