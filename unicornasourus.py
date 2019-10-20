ar=[[1,3],[6,8],[11,12]]
reduc=[]
last=0
val=0
for i in range(len(ar)):
    for j in range(ar[i][0]-last-1):
        reduc.append(val)
    for j in range(ar[i][1]-ar[i][0]+1):
        val+=1
        reduc.append(val)
    last= ar[i][1]

print(reduc)