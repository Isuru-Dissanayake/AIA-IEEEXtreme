#https://csacademy.com/ieeextreme-practice/task/ed8629419f140a5a2c923b049aba1224/

def maxPower(w, g, w_num):
    power = 0
    
    

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
    