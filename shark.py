n= 3
ar=[]
for i in range(n*4):
    arr= [char for char in str(input())]
    while len(arr)!= (n-1)*20:
        arr.append(' ')
    for j in range(len(arr)):
        if arr[j]=='M':
            arr[j]=1
        else:
            arr[j]=0


    ar.append(arr) 
print (ar)
import numpy as np
ar= np.array(ar)
from skimage.transform import resize
shark_resized = resize(ar, (16, 60))
print(shark_resized)