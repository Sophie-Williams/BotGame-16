'''
Created on Aug 23, 2016

@author: TDARSEY
'''

import util

from Board.board import Board
from Board.piece import Bot, Food
from Board.enum import Direction
import random

import time

directions = [
    Direction.up,
    Direction.down, 
    Direction.left, 
    Direction.right]

myBoard = Board()
myBot = Bot()
myBoard.setSquare((1, 1), myBot)

clock = 0

flipint = 500
    
def flip():
    util.clear()
    print myBoard

def tick():
    
    if(random.randint(0, 100) == 50):
        myBoard.setSquare((
                               random.randint(0, myBoard._size[0] - 1), 
                               random.randint(0, myBoard._size[1] - 1)), 
                            Food())
    myBot.move(random.choice(directions))
    
while(True):
    clock += 1
    tick()
    
    if(clock % flipint == 0):
        flip()

    #time.sleep(0.03)