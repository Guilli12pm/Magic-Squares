import numpy as np
import time

class Square:
    def __init__(self,n,time,show):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.counter = 0
        self.n = n
        self.times = time
        self.show = show

    def print_board(self):
        for _ in range(4):
            print("\n")

        maxl = len(str(self.n ** 2))
        for j in range(self.n):
            for i in range(self.n):
                if self.board[j][i] == 0:
                    print(" " * maxl, end=" ")
                else:
                    lenw = len(str(self.board[j][i]))
                    print(" " * (maxl - lenw) + str(self.board[j][i]), end=" ")
            print()
        

    def add_board(self):
        i,j = int(self.n // 2),0
        while self.counter < self.n**2:
            self.counter += 1
            self.board[j][i] = self.counter

            if self.show:
                self.print_board()

            if i == self.n - 1:
                if self.board[j-1][0] != 0:
                    j += 1
                else:
                    if i+1 > self.n - 1:
                        i = 0
                    else:
                        i += 1
                    
                    if j-1 < 0:
                        j = self.n - 1
                    else:
                        j -= 1                   

            elif j == 0:
                if self.board[self.n - 1][i+1] != 0:
                    j += 1
                else:
                    if i+1 > self.n - 1:
                        i = 0
                    else:
                        i += 1
                    
                    if j-1 < 0:
                        j = self.n - 1
                    else:
                        j -= 1


            elif self.board[j-1][i+1] != 0:
                j += 1
                
            else:
                if i+1 > self.n - 1:
                    i = 0
                else:
                    i += 1
                
                if j-1 < 0:
                    j = self.n - 1
                else:
                    j -= 1

            if self.times != False:
                time.sleep(self.times)

    def check(self):
        print("\n")
        print("The sum of columns =",[sum(self.board[j]) for j in range(self.n)])
        print("The sum of rows =",[sum([self.board[j][i] for i in range(self.n)]) for j in range(self.n)])

#### Show board at each step ####
show = False

#### Slow the showing at each step, False for no time and any number for time in seconds ####
times = False

#### Size of board ####
n = 7 

a = Square(n,times,show)
a.add_board()
a.print_board()
a.check()