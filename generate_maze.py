# -*- coding: utf-8 -*-
"""
Created on Mon May  3 15:58:45 2021

@author: dell

Maze generation
Idea: use Prim's Algorithm
http://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm.html
"""

import random



"""
    w, h are even
"""
def generate_board(w: int=9, h: int=9):
    assert w%2!=0 and h%2!=0
    board = [[0 if i*j%2 != 0 else 1 for j in range(w) ] for  i in range(h)]
    return board


        

def count_zeros(board):
    count = 0
    for row in board:
        count += row.count(0)
    return count

def union(x, y):
    global parent
    x, y = find(x), find(y)
    if x == y:
        return x
    parent[y] = x

def find(x):
    global parent, board
    root = x 
    while True:
        p = parent[root]
        if p == root:
            break
        root = p
        
    current = x
    while current != root:
        next_elem = parent[current]
        parent[current] = root
        current = next_elem
    
    return root
    
def generate_maze(w=9, h=9):
    global parent, board
    board = generate_board(w, h)
    parent = [i for i in range(w*h)]
    x = w+1
    merged = [x]
    
    #number of 'nodes' in the 'spanning tree'
    N = count_zeros(board)
    while len(merged) < N:
        idx = random.randint(0, len(merged)-1)
        x = merged[idx]
        
        i, j = x//w, x%w
        
        direction = random.randint(0,3)
        
        if direction == 0 and i>1:
            y = (i-2)*w + j
            x_, y_ = find(x), find(y)
            if x_ != y_:
                board[i-1][j] = 0
                merged.append(y)
                parent[y_] = x_
                continue
            
        direction = random.randint(1,3)
        
        if direction == 1 and i+2 < h:
            y= (i+2)*w + j
            x_, y_ = find(x), find(y)
            if x_ != y_:
                board[i+1][j] = 0
                merged.append(y)
                parent[y_] = x_
                continue
            
        direction = random.randint(2,3)
        
        if direction == 2 and j > 1:
            y = i*w + j-2
            x_, y_ = find(x), find(y)
            if x_ != y_:
                board[i][j-1] = 0
                merged.append(y)
                parent[y_] = x_
                continue
            
        direction = 3
        
        if direction == 3 and j+2 < w:
            y= i*w + j+2
            x_, y_ = find(x), find(y)
            if x_ != y_:
                board[i][j+1] = 0
                merged.append(y)
                parent[y_] = x_
                continue
        
        
    return board
        

generate_maze(19, 11)
#board = generate_board(5, 11)

for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end=' ')
    print()
#%%