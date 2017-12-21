import timeit
import numpy as np
import random
import sys 
import copy
from optparse import OptionParser as op
import queen_dfs
import queen_hill1

print "*****************",'\n',"Choose options to solve N-queen problem",'\n',"1:DFS",'\n',"2:Hill Climbing"
choice=int(input("\n"))


if choice==1:
 start=timeit.default_timer()
 queen_dfs.searchCol(0);
 print queen_dfs.sols
 stop=timeit.default_timer()
 time=stop-start
 print "time complexity",time
else:
 start1=timeit.default_timer()
 parser = op()
 parser.add_option("-e", "--exit", dest="move_style",
                   action="store_false", default=True)
 
 parser.add_option("--moves", dest="moves",default=1,
                   type="int")
 
 (options, args) = parser.parse_args()
 
 temp_board = queen_hill1.queens(move_style=options.move_style, moves=options.moves)
 temp_board.printstats()
 stop1=timeit.default_timer()
 time1=stop1-start1
 print "time complexity",time1
 


