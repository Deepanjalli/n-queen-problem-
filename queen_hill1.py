import numpy as np
import random
import sys 
import copy
from optparse import OptionParser as op


class chess_board:
  def __init__(self, list=None):                                                                          
    if list == None:
      self.chess_board = [[0 for i in range(0,8)] for j in range(0,8)]
      #initialize queens at random places
      for i in range(0,8):
        while 1:
          row = random.randint(0,7)
          col = random.randint(0,7)
          if self.chess_board[row][col] == 0:
            self.chess_board[row][col] = "1"
            break
    # print errors if chess_board is not right format or dimension
  #print the chess_board
  def __repr__(self):
    temp_str = ""
    for i in range(0,8):
      for j in range(0,8):
        temp_str = temp_str + str(self.chess_board[i][j]) + " "
      temp_str = temp_str + "\n"
    return (temp_str)

class queens:
  def __init__(self, moves, move_style, chess_board1=None):
    #verify options
    self.total_moves = moves
    self.succ = 0
    self.steps = 0
    self.move_style = move_style
    for i in range(0,moves):
      if self.move_style == True:
        print '\n'
      self.temp_board = chess_board(chess_board1)
      self.cost = self.cost1(self.temp_board)
      self.hill_climbing()
 
  def hill_climbing(self):
    while 1:
      attacks = self.cost
      self.min_cost_board()
      if attacks == self.cost:
        break
      self.steps += 1
      if self.move_style == True:
        print "Queen attacks", self.cost1(self.temp_board)
        print self.temp_board
    if self.cost != 0:
      if self.move_style == True:
        print "Null"
    else:
      self.succ += 1
    return self.cost
 
  def printstats(self):
    print "Moves: ", self.total_moves,'\t',"Success: ", self.succ,'\t',"number of steps: ",self.steps 
 
  def cost1(self, temp_board1):
    #heuristic cost
    heur_cost = 0
    dist_cost = 0
    for i in range(0,8):
      for j in range(0,8):
        #calculate all violations if this node is queen
        if temp_board1.chess_board[i][j] == "1":
          #2 for subtracting horizontal and vertical moves
          heur_cost -= 2
          for m in range(0,8):
            if temp_board1.chess_board[i][m] == "1":
              heur_cost += 1
            if temp_board1.chess_board[m][j] == "1":
              heur_cost += 1
          #diagonal violations
          m, p = i+1, j+1
          while m < 8 and p < 8:
            if temp_board1.chess_board[m][p] == "1":
              dist_cost += 1
            m +=1
            p +=1
          m, p = i+1, j-1
          while m < 8 and p >= 0:
            if temp_board1.chess_board[m][p] == "1":
              dist_cost += 1
            m +=1
            p -=1
          m, p = i-1, j+1
          while m >= 0 and p < 8:
            if temp_board1.chess_board[m][p] == "1":
              dist_cost += 1
            m -=1
            p +=1
          m, p = i-1, j-1
          while m >= 0 and p >= 0:
            if temp_board1.chess_board[m][p] == "1":
              dist_cost += 1
            m -=1
            p -=1
    return ((dist_cost + heur_cost)/2)
  
  def min_cost_board(self):
    minc = self.cost1(self.temp_board)
    minc1 = self.temp_board
    #move one queen at a time
    for row1 in range(0,8):
      for col1 in range(0,8):
        if self.temp_board.chess_board[row1][col1] == "1":
          #get the lowest cost by moving this queen
          for row2 in range(0,8):
            for col2 in range(0,8):
              if self.temp_board.chess_board[row2][col2] != "1":
                #place queen and check if it's any better
                temp_board2 = copy.deepcopy(self.temp_board)
                temp_board2.chess_board[row1][col1] = 0
                temp_board2.chess_board[row2][col2] = "1"
                cost1 = self.cost1(temp_board2)
                if cost1 < minc:
                  minc = cost1
                  minc1 = temp_board2
    self.temp_board = minc1
    self.cost = minc



 



