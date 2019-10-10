'''class Graph: 
  
    def __init__(self, row, col, g): 
        self.ROW = row 
        self.COL = col 
        self.graph = g 
  
    # A function to check if a given cell  
    # (row, col) can be included in DFS 
    def isSafe(self, i, j, visited): 
        # row number is in range, column number 
        # is in range and value is 1  
        # and not yet visited 
        return (i >= 0 and i < self.ROW and 
                j >= 0 and j < self.COL and 
                not visited[i][j] and self.graph[i][j]) 
              
  
    # A utility function to do DFS for a 2D  
    # boolean matrix. It only considers 
    # the 8 neighbours as adjacent vertices 
    def DFS(self, i, j, visited): 
  
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]; 
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]; 
          
        # Mark this cell as visited 
        visited[i][j] = True
  
        # Recur for all connected neighbours 
        for k in range(8): 
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited): 
                self.DFS(i + rowNbr[k], j + colNbr[k], visited) 
  
  
    # The main function that returns 
    # count of islands in a given boolean 
    # 2D matrix 
    def countIslands(self): 
        # Make a bool array to mark visited cells. 
        # Initially all cells are unvisited 
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)] 
  
        # Initialize count as 0 and travese  
        # through the all cells of 
        # given matrix 
        count = 0
        for i in range(self.ROW): 
            for j in range(self.COL): 
                # If a cell with value 1 is not visited yet,  
                # then new island found 
                if visited[i][j] == False and self.graph[i][j] == 1: 
                    # Visit all cells in this island  
                    # and increment island count 
                    self.DFS(i, j, visited) 
                    count += 1
  
        return count 
  
  


def neighbours_plus(x,y,pic):
    lis=[]
    if x+1<l:
        if pic[y][x+1]==1:
            lis.append([x+1,y])
    if x-1>=0:
        if pic[y][x-1]==1:
            lis.append([x-1,y])
    if y-1>=0:
        if pic[y-1][x]==1:
            lis.append([x,y-1])
    if y+1<h:
        if pic[y+1][x]==1:
            lis.append([x,y+1])
    return lis

def neighbours_cross(x,y,pic):
    lis=[]
    if x+1<l:
        if y+1<h:
            if pic[y+1][x+1]==1:
                lis.append([x+1,y+1])
        if y-1>=0:
            if pic[y-1][x+1]==1:
                lis.append([x+1,y-1])
    if x-1>=0:
        if y+1<h:
            if pic[y+1][x-1]==1:
                lis.append([x-1,y+1])
        if y-1>=0:
            if pic[y-1][x-1]==1:
                lis.append([x-1,y-1])
    return lis
    

ntests= int(input())
for i in range(ntests):
    l,h= list(map(int,input().strip().split(' ')))
    picture=[]
    for j in range(h):
        n = str(input().strip())
        row = [int(i) for i in n]
        picture.append(row)
        
    graph = [a[:] for a in picture]
    row = len(graph) 
    col = len(graph[0]) 
    g = Graph(row, col, graph) 
    
    pic1 = [a[:] for a in picture]
    q=[]
    crossCount1=0
    for j in range(h):
        for k in range(l):
            if pic1[j][k]==1:
                crossCount1+=1
                q.append([k,j])
                while len(q)>0:
                    crux,cruy=q.pop(-1)
                    pic1[cruy][crux]=0
                    listy= neighbours_plus(crux,cruy,pic1)
                    if len(listy)==0:
                        pass
                    for r in listy:
                        #if pic1[r[1]][r[0]]==1:
                        q.append(r)
    

    pic2 = [a[:] for a in picture]
    q=[]
    crossCount2=0
    
    for j in range(h):
        for k in range(l):
            if pic2[j][k]==1:
                crossCount2+=1
                q.append([k,j])
                while len(q)>0:
                    crux,cruy=q.pop(-1)
                    pic2[cruy][crux]=0
                    listy= neighbours_cross(crux,cruy,pic2)
                    if len(listy)==0:
                        pass
                    for r in listy:
                        #print(r)
                        #if pic2[r[1]][r[0]]==1:
                        q.append(r)

    pic3 = [a[:] for a in picture]
    q=[]
    crossCount3=0
    
    for j in range(h):
        for k in range(l):
            if pic3[j][k]==1:
                crossCount3+=1
                q.append([k,j])
                while len(q)>0:
                    crux,cruy=q.pop(-1)
                    pic3[cruy][crux]=0
                    listy= neighbours_cross(crux,cruy,pic3)+neighbours_plus(crux,cruy,pic3)
                    if len(listy)==0:
                        pass
                    for r in listy:
                        #print(r)
                        #if pic2[r[1]][r[0]]==1:
                        q.append(r)
  
  
    
    
    print (crossCount1,crossCount3)#, g.countIslands() )
    
'''    

    
def neighbours_plus(x,y,pic):
    lis=[]
    if x+1<l:
        if pic[y][x+1]==1:
            lis.append([x+1,y])
    if x-1>=0:
        if pic[y][x-1]==1:
            lis.append([x-1,y])
    if y-1>=0:
        if pic[y-1][x]==1:
            lis.append([x,y-1])
    if y+1<h:
        if pic[y+1][x]==1:
            lis.append([x,y+1])
    return lis

def neighbours_cross(x,y,pic):
    lis=[]
    if x+1<l:
        if y+1<h:
            if pic[y+1][x+1]==1:
                lis.append([x+1,y+1])
        if y-1>=0:
            if pic[y-1][x+1]==1:
                lis.append([x+1,y-1])
    if x-1>=0:
        if y+1<h:
            if pic[y+1][x-1]==1:
                lis.append([x-1,y+1])
        if y-1>=0:
            if pic[y-1][x-1]==1:
                lis.append([x-1,y-1])
    return lis
    

ntests= int(input())
for i in range(ntests):
    l,h= list(map(int,input().strip().split(' ')))
    picture=[]
    for j in range(h):
        n = str(input().strip())
        row = [int(i) for i in n]
        picture.append(row)
        
    
    pic1 = [a[:] for a in picture]
    q1=[]
    crossCount1=0
    for j in range(h):
        for k in range(l):
            if pic1[j][k]==1:
                crossCount1+=1
                q1.append([k,j])
                while len(q1)>0:
                    crux,cruy=q1.1pop(-1)
                    pic1[cruy][crux]=0
                    listy= neighbours_plus(crux,cruy,pic1)
                    if len(listy)==0:
                        pass
                    for r in listy:
                        q1.append(r)
    

    pic2 = [a[:] for a in picture]
    q=[]
    crossCount2=0
    
    for j in range(h):
        for k in range(l):
            if pic2[j][k]==1:
                crossCount2+=1
                q.append([k,j])
                while len(q)>0:
                    crux,cruy=q.pop(-1)
                    pic2[cruy][crux]=0
                    listy= neighbours_cross(crux,cruy,pic2)
                    if len(listy)==0:
                        pass
                    for r in listy:
                        q.append(r)

    pic3 = [a[:] for a in picture]
    q=[]
    crossCount3=0
    
    for j in range(h):
        for k in range(l):
            if pic3[j][k]==1:
                crossCount3+=1
                q.append([k,j])
                while len(q)>0:
                    crux,cruy=q.pop(-1)
                    pic3[cruy][crux]=0
                    listy= neighbours_cross(crux,cruy,pic3)+neighbours_plus(crux,cruy,pic3)
                    if len(listy)==0:
                        pass
                    for r in listy:
                        q.append(r)
 
 
    print (crossCount1,crossCount2, crossCount3)
   

