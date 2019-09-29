#https://csacademy.com/ieeextreme-practice/task/ed8629419f140a5a2c923b049aba1224/
def maxPower(w, g, w_num):
    power = [[0 for i in range(len(w))] for i in range(w_num+1)]
    for i in range(len(w)):
        for j in range(w_num+1):
            if i == 0:
                if j >= w[i]:
                    power[j][i] = g[i]
            else:
                if j >= w[i]:
                    empty = j -w[i]
                    power[j][i] = max(power[empty]) + g[i]

    print (max(power[-1]))
'''
def maxPower(w, g, w_num):
    power = [[0 for i in range(w_num+1)] for i in range(len(w))]
    #print (power)
    for i in range(len(w)):
        for j in range(w_num+1):
            if i == 0:
                if j >= w[i]:
                    power[i][j] = g[i]
            else:
                if j >= w[i]:
                    empty = j - w[i]
                    emptyArr = []
                    for v in range(i):
                        emptyArr.append(power[v][empty])
                    power[i][j] = max(emptyArr) + g[i]
        #print (power)
    powerArr = []
    for i in range(len(w)):
        powerArr.append(power[i][w_num])
    #print (power)
    print (max(powerArr))
'''
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