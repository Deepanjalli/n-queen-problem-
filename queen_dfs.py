import numpy as np
N=int(input('no. of queens for DFS\n'));
board=np.zeros((N,N));
numQueens =0;
sols =0;

def searchCol(col):
 global numQueens
 global sols
 if(numQueens >=N):
  print board,'\n'
  sols+= 1;
  return
 for i in range(N):
  if (board[i,col] > -1):   ##########assign quuen to 1st cell of board
   board[i,col] = 1;
   for j in range(N):
    if (j != col):          ########cells which do not have same column as the previous queen decrease their value by 1
     board[i,j]-=1;
    if (j != i):            ########cells which do not have same row as the previous queen decrease their value by 1
     board[j,col]-=1;        
   for j in range(1,N):        
    if ((i-j) >=0) and ((col-j) >=0):              ######cells which are not diagonal to the previous queen decrease their value by 1
     board[i-j,col-j]-=1;
    if ((i+j) <N) and ((col+j) <N):
     board[i+j,col+j]-=1;
    if ((i-j) >=0) and ((col+j) <N):
     board[i-j,col+j]-=1;
    if ((i+j) <N) and ((col-j) >=0):
     board[i+j,col-j]-=1;
   numQueens+=1;                                             
   searchCol(col+1);                   ########repeat recursively for other columns
   board[i,col] =0;                    
   for j in range(N):                    ########cells which do not have same column as the previous queen increase their value by 1
    if(j != col):
     board[i,j]+=1;
    if(j !=i):                             ########cells which do not have same row as the previous queen increase their value by 1
     board[j,col]+=1;
   for j in range(1,N):
    if ((i-j) >=0) and ((col -j) >=0):
     board[i-j,col-j]+=1;
    if ((i+j) <N) and ((col +j) <N):        ######cells which are not diagonal to the previous queen increase their value by 1
     board[i+j,col+j]+=1;
    if ((i-j) >=0) and ((col +j) <N):
     board[i-j,col+j]+=1;
    if ((i+j) <N) and ((col -j) >=0):
     board[i+j,col-j]+=1;
   numQueens-=1;                      ##########if no solution found then replace the queen and backtrack

###searchCol(0);
##print sols;

