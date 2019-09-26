#https://csacademy.com/ieeextreme-practice/task/8761fb7efefcf1d890df1d8d91cae241/

m = int(input(""))
n = []
h = []
for q in range(m):
    name, height = list(map(str,(input("")).split()))
    n.append(name)
    h.append(int(height))
def findWay(n,h):
    h_sorted = sorted(list(dict.fromkeys(h)))
    arr_n = []
    arr_h = []
    ans = ""
    for i in range(len(h_sorted)):
        for j in range(len(h)):
            if (h_sorted[i] == h[j]):
                arr_n.append(n[j])
                arr_h.append(h[j])
    
    t = arr_h[0]
    s = 1
    e = 1 
    eq = [arr_n[0]]
    for i in range(1,len(arr_h)): 
        if arr_h[i] == t:
            t = arr_h[i]
            eq.append(arr_n[i])
            e = i + 1
            pass
        else:
            e = i
            eq = sorted(eq)
            ans = ans + " ".join(eq) + str(" ") + str(s) + str(" ") + str(e) + str("\n")
            eq = []
            s = i + 1
            t = arr_h[i]
            eq.append(arr_n[i])
    eq = sorted(eq)
    ans = ans + " ".join(eq) + str(" ") + str(s) + str(" ") + str(e) + str("\n")
    #print (arr_n)
    #print (arr_h)
    print (ans)
            

findWay(n,h)