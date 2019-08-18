def maxSubarray(array):
    subarraySum = 0
    subsquenceSum = 0
    subarraySumMax = 0
    arrayNew = array[::-1]
    count = 0
    for i in range(len(array)):
        if (arrayNew[i] > 0):
            arrayNew = arrayNew[i:]
            count = 1
            break
    if (count == 0):
        return (max(array),max(array))
    else:
        arrayNew = arrayNew[::-1]
        i = 0
        while (i < len(arrayNew)):
            if (arrayNew[i] > 0):
                subarraySum = subarraySum + arrayNew[i]
                subsquenceSum += arrayNew[i]
                i+=1
            elif ((subarraySum >= arrayNew[i]) and (arrayNew[i+1] >= arrayNew[i])):
                subarraySum = subarraySum + arrayNew[i] + arrayNew[i+1]
                subsquenceSum += arrayNew[i+1]
                i+=2
            elif (subarraySum <= arrayNew[i]):
                subarraySumMax = max(subarraySumMax,subarraySum)
        subarraySumMax = max(subarraySum,subarraySumMax)
        return (subarraySumMax, subsquenceSum)

array = [2, -1, 2, 3, 4, -5]
a, b = maxSubarray(array)
ans = str(a) + " " + str(b)
print (ans)
            