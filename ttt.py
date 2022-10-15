import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1='X'
p2='O'

def place(symbol):
 print(numpy.matrix(board))
 while(1):
  r=int(input('enter the row'))
  c=int(input('enter the col'))
  if r<4 and c<4 and board[r-1][c-1]=='-':
     break
  else:
     print('invalid input')
 board[r-1][c-1]=symbol

def won(symbol):
    return row(symbol) or col(symbol) or dia(symbol)

def row(symbol):
 count=0
 for i in range(3):
        for j in range(3):
            if board[i][j]==symbol:
             count=count+1
             
 if count==3:
    return True
 else:
    return False 

def col(symbol):
 count=0
 for j in range(3):
        for i in range(3):
            if board[i][j]==symbol:
             count=count+1

 if count==3:
    return 1
 else:
    return 0

def dia(symbol):
    if  board[0][2]== board[1][1] and  board[1][1]== board[2][0] and board[1][1]!='-':
        return 1
    if  board[0][0]== board[1][1] and  board[1][1]== board[2][2] and board[1][1]!='-':
        return 1
    else:
     return 0        

def play():
 turn=0
 for i in range(9):
        if turn%2==0:
            print('player 1 turn')
            place(p1)
            turn=turn+1
            if(won(p1)):
                print('p1 won')
                break
        else:
            print('player 2 turn')
            place(p2)
            turn=turn+1
            if(won(p2)):
                print('p2 won')
                break  
 if not won(p1) or won(p2):
  print('draw')  

play()
