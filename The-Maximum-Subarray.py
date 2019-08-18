def maxSubarray(array):
    subarraySum = 0
    subsquenceSum = 0
    subarraySumMax = 0
    count = 0

    arrayNew = array[::-1]
    for i in range(len(array)):
        if (arrayNew[i] > 0):
            arrayNew = arrayNew[i:]
            break
    if (i == len(array)):
        return (max(array),max(array))
    else:
        arrayNew = arrayNew[::-1]

        for i in range(len(arrayNew)):
            if (arrayNew[i] >= 0):
                subarraySum += arrayNew[i]
                subsquenceSum += arrayNew[i]
            elif (subarraySum > arrayNew[i]):
                subarraySum += arrayNew[i]
                count +=1
            elif (subarraySum < arrayNew[i]):
                subarraySumMax = max(subarraySum,subarraySumMax)
                subarraySum = 0
                count +=1
        if count == len(arrayNew):
            subarraySumMax = subsquenceSum = max(array)
        
        return (subarraySumMax, subsquenceSum)

array = [2, -1, 2, 3, 4, -5]
a, b = maxSubarray(array)
ans = str(a) + " " + str(b)
print (ans)
            