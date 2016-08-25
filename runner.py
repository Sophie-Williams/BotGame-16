'''
Created on Aug 23, 2016

@author: TDARSEY
'''

import util

from Board.board import Board, Square

import random

import time

myBoard = Board()

def tick():
    #char = random.sample(set(["X", "O", " "]), 1)[0]
    #myBoard.setSquare((5, 1), char)
    
    util.clear()
    print myBoard


while(True):
    tick()
    time.sleep(0.06)

print myBoard