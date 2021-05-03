# -*- coding: utf-8 -*-
"""
Created on Mon May  3 18:45:39 2021

@author: dell

Maze generation
Idea: Kruskal algorithm
http://weblog.jamisbuck.org/2011/1/3/maze-generation-kruskal-s-algorithm
"""


import random
from tkinter import *


"""
    w, h are even
    board is also parent in union-join. Tuple (i,j) represents the parent of this current cell
    1 means dead end and 0 means path
"""
def generate_board(w: int=9, h: int=9):
    assert w%2!=0 and h%2!=0
    board = [[(i, j) if i*j%2 != 0 else 1 for j in range(w) ] for  i in range(h)]
    return board


def find(x):
    global board
    root = x 
    while True:
        p = board[root[0]][root[1]]
        if p == root:
            break
        root = p
        
    current = x
    while current != root:
        next_elem = board[current[0]][current[1]]
        board[current[0]][current[1]] = root
        current = next_elem
    
    return root
    
def generate_maze(w=9, h=9):
    global parent, board, edges
    
    board = generate_board(w, h)    
    
    #Based on Kruskal algorithm. Cells that not contain 1 are 'nodes'
    #Store list of 'edges' and pop it gradually to build the 'spanning tree'
    #edges are cells with number 1, either i or j is even (i+j%2==1)    
    edges = [(i, j) for j in range(1, len(board[0])-1) for i in range(1, len(board)-1) if (i+j)%2==1]
    random.shuffle(edges)
    
    while edges:
        i, j = edges.pop()
        
        #'horizontal edge'
        if i%2 != 0:
            #left cell
            x = (i, j-1)
            #right cell
            y = (i, j+1)
        
        #'vertical edge'
        else:
            #left cell
            x = (i-1, j)
            #right cell
            y = (i+1, j)
        
        x, y = find(x), find(y)
        if x != y:
            board[i][j] = 0
            board[y[0]][y[1]] = x
            
            
    board = [ [elem if elem==1 else 0 for elem in row] for row in board]   
    
        
       
    return board
        

board = generate_maze(19, 19)

def print_maze(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()
#%%


  
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
