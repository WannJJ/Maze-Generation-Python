# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:58:45 2021

@author: dell


Maze generation
Method: Recursive Division
http://weblog.jamisbuck.org/2011/1/12/maze-generation-recursive-division-algorithm.html
"""

import random
from tkinter import *

#Create an empty board with 0s in a frame of 1s
def generate_board(w: int=9, h: int=9):
    assert w%2!=0 and h%2!=0
    board = [[1 if i==0 or j==0 or i==h-1 or j==w-1 else 0 for j in range(w) ] for  i in range(h)]
    return board

def rec_div(board, i1, i2, j1, j2):
    i1 = i1 if i1 % 2 != 0 else i1 + 1
    i2 = i2 if i2 % 2 != 0 else i2 - 1
    #amount of odd numbers between i1 and i2
    n_i = (i2-i1)//2 + +1
    
    j1 = j1 if j1 % 2 != 0 else j1 + 1
    j2 = j2 if j2 % 2 != 0 else j2 - 1
    #amount of odd numbers between i1 and i2
    n_j = (j2-j1)//2 + 1
    
    if n_i == 1:
        i = i1 
        for j in [j for j in range(j1, j2)]:
            board[i][j] = 0 
        return
    
    if n_j == 1:
        j = j1 
        for i in [i for i in range(i1, i2)]:
            board[i][j] = 0
        return
    
    if n_i >= n_j:
        i = i1 + random.randint(1,n_i-1) * 2 -1
        for j in range(j1, j2+1):
            board[i][j] = 1
        j = random.randint(j1, j2)
        if j%2==0:
            j+=1
        board[i][j] = 0
        rec_div(board, i1, i-1, j1, j2)
        rec_div(board, i+1, i2, j1, j2)
        return
    
    else:
        j = j1 + random.randint(1, n_j-1) * 2 -1
        for i in range(i1, i2+1):
            board[i][j] = 1
        i = random.randint(i1, i2)
        if i%2==0:
            i+=1
        board[i][j] = 0
        rec_div(board, i1, i2, j1, j-1)
        rec_div(board, i1, i2, j+1, j2)
    
 



    

def generate_maze(w=9, h=9):
    board = generate_board(w, h)
    rec_div(board, 0, h-1, 0, w-1)
    
    return board

board = generate_maze(11, 15)

def visualize_maze(board, x0=5, y0=5, a=30):
    root = Tk()
      
    C = Canvas(root, bg ="yellow",
               height = 300, width = 300)
    
    
    
      
    x0, y0 = 5,5
    a = 30
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1 and (i+j)%2 != 0:
                if i%2 == 0:
                    i_ = i//2
                    j = (j-1)//2
                    C.create_line(x0+ a*j, y0+ a*i_, x0+ a*(j+1), y0+a*i_,fill ="black")
                
                else:
                    j = j//2
                    i_ = (i-1)//2
                    C.create_line(x0+ a*j, y0+ a*i_, x0+ a*j, y0+a*(i_+1),fill ="black")
  

  
    C.pack()
    mainloop()
#%%
    
    
#directly draw a maze using tkinter
  
  
root = Tk()
  
C = Canvas(root, bg ="yellow",
           height = 300, width = 300)

x0, y0 = 5,5
a = 30

def rec_draw_maze(x, y, w, h, vertical = True):
    if w == 1 or h == 1:
        return
    
    i = random.randint(1, w-1)
    j = random.randint(1, h-1)
    if vertical:
        C.create_line(x + a*i, y, x + a*i, y + a*j , fill ="black")
        C.create_line(x + a*i, y + a*(j+1), x + a*i, y + a*h , fill ="black")
        rec_draw_maze(x, y, i, h, False)
        rec_draw_maze(x+a*i, y, w - i, h, False)
    else:
        C.create_line(x, y + a*j, x + a*i, y + a*j , fill ="black")
        C.create_line(x + a*(i+1), y + a*j, x + a*w, y + a*j , fill ="black")
        rec_draw_maze(x, y, w, j)
        rec_draw_maze(x, y + a*j, w, h - j)

def generate_maze2(w=9, h=9):
    C.create_line(x0, y0,x0 + a*w, y0,fill ="black")
    C.create_line(x0 + a*w, y0,x0 + a*w, y0 + a*h,fill ="black")
    C.create_line(x0, y0,x0, y0 + a*h,fill ="black")
    C.create_line(x0, y0 + a*h,x0 + a*w, y0 + a*h,fill ="black")
    
    rec_draw_maze(x0, y0, w, h)
    

generate_maze2()
    

C.pack()
mainloop()