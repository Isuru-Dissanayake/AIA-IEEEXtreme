#https://csacademy.com/ieeextreme-practice/task/ed8629419f140a5a2c923b049aba1224/

def findMethods(n):
    indexArr = []
    if n%2 == 0:
        for r in range(1,int(n/2) - 1):
            arr1 = []
            arr1.append(r)
            arr1.append(n-r)
            indexArr.append(arr1)
    if n%2 == 1:
        for r in range(1,int(n/2)):
            arr1 = []
            arr1.append(r)
            arr1.append(n-r)
            indexArr.append(arr1)
    return (indexArr)

def maxPower(w, g, w_num):
    power = [0 for e in range(w_num+1)]
    for k in range(len(power)):
        for j in range(len(w)):
            if w[j] == k:
                power[k] = max(power[k],g[j])
    print (power)
    for k in range(len(power)):
        indexArr = findMethods(k)
        for f in range(len(indexArr)):
            num1 = power[indexArr[f][0]]
            num2 = power[indexArr[f][1]]
            power[k] = max(power[k],(num1+num2))
    print (power)

t = int(input(""))
for testCases in range(t):
    wg = list(map(int,input("").split()))
    w_num = wg[0]
    g_num = wg[1]
    w = []
    g = []
    for i in range(g_num):
        wg = list(map(int,input("").split()))
        w.append(wg[0])
        g.append(wg[1])
    maxPower(w, g, w_num)