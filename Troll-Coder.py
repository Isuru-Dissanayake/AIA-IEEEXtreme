def communicate(arr):
    msg = "Q " + " ".join(arr)
    print (msg)
    return (int(input("")))

n = int(input(""))
arr = ["0"] * n
truLast = communicate(arr)
if (truLast == n):
    msg= "A " + " ".join(arr)
    print (msg)
else:
    if n%2 == 0:
        i = 0
        while (1):
            arr[i] = "1"
            arr[i+1] = "1"
            tru = communicate(arr)
            if (tru == truLast -2):
                arr[i] = "0"
                arr[i+1] = "0"
            elif (tru == truLast):
                arr[i] = "1"
                arr[i+1] = "0"
                tru = communicate(arr)
                if (tru < truLast):
                    arr[i] = "0"
                    arr[i+1] = "1"
                truLast = truLast + 1
            elif (tru > truLast):
                truLast = truLast + 2
            i = i + 2
            if (truLast == n):
                msg= "A " + " ".join(arr)
                print (msg)
                break
    else:
        arr.append(0)
        i = 0
        while (1):
            arr[i] = 1
            arr[i+1] = 1
            tru = communicate(arr[:-1])
            if (tru == truLast -2):
                arr[i] = 0
                arr[i+1] = 0
            elif (tru == truLast):
                arr[i] = 1
                arr[i+1] = 0
                tru = communicate(arr[:-1])
                if (tru < truLast):
                    arr[i] = 0
                    arr[i+1] = 1
                truLast = tru + 1
            elif (tru > truLast):
                truLast = truLast + 2
            if (truLast == n):
                msg= "A " + " ".join(arr)
                print (msg)
                break   

