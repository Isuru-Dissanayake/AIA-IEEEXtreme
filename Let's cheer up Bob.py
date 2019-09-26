def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
winSets=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

def win(arr):
    bobMoves=[]
    for i in range(len(arr)):
        if (i%2==0):
            bobMoves.append(arr[i])
    for i in winSets:   
        if(all(x in bobMoves for x in i)): 
            return True
            
    return False
        
   
import numpy
import scipy
Bob=[]
moves=[]
for i in range(9):
    a = get_number()
    b = get_number()
    Bob.append((a-1)*3+ b)



def findMoves():   
    move=[Bob[0]]
    for i in range(1,10):
        move1= move.copy()
        if (i not in move1):
            move1.append(i)
            moves.append(move1)
            
    
    for j in range(8):
        move2= moves[j].copy()
        for k in range(9):
            if (Bob[k] not in move2):
                move2.append(Bob[k])
                moves[j]=move2
                break
    
    for j in range(8):
        moves3=[]
        for k in range(1,10):
            if (k not in moves[j]):
                move3= moves[j].copy()
                move3.append(k)
                moves3.append(move3)
        moves[j]=moves3
    
    for j in range(8):
        for k in range(6):
            move4= moves[j][k].copy()
            for m in range(9):
                if (Bob[m] not in move4):
                    move4.append(Bob[m])
                    if win(move4):
                        myMoves(move4)
                        return
                    else:
                        moves[j][k]= move4
                    break
            
    for j in range(8):
        for i in range(6):
            moves3=[]
            for k in range(1,10):
                if (k not in moves[j][i]):
                    move3= moves[j][i].copy()
                    move3.append(k)
                    moves3.append(move3)
            moves[j][i]=moves3
        
    for j in range(8):
        for k in range(6):
            for q in range(4):
                move4= moves[j][k][q].copy()
                for m in range(9):
                    if (Bob[m] not in move4):
                        move4.append(Bob[m])
                        if win(move4):
                            myMoves(move4)
                            return
                        else:
                            moves[j][k][q]= move4
                        break   
                    
    for j in range(8):
        for i in range(6):
            for q in range(4):
                moves3=[]
                for k in range(1,10):
                    if (k not in moves[j][i][q]):
                        move3= moves[j][i][q].copy()
                        move3.append(k)
                        moves3.append(move3)
                moves[j][i][q]=moves3
                
    for j in range(8):
        for k in range(6):
            for q in range(4):
                for r in range(2):
                    move4= moves[j][k][q][r].copy()
                    for m in range(9):
                        if (Bob[m] not in move4):
                            move4.append(Bob[m])
                            if win(move4):
                                myMoves(move4)
                                return
                            else:
                                moves[j][k][q][r]= move4
                            break

def myMoves(arr):
    for i in range(len(arr)):
        if (i%2==1):
            a= arr[i]%3
            if (a==0):
                a=3
            print (((arr[i]-1)//3)+1, a )
findMoves()