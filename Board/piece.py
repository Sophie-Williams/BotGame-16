'''
Created on Aug 25, 2016

@author: TDARSEY
'''

from enum import Direction

class aPiece(object):
    char = '?'
    def __init__(self, board = None, pos = None):
        self.board = board
        self.pos = pos
    
    def __str__(self):
        return self.char
    
class Block(aPiece):
    char = "X"
    
class Bot(aPiece):
    char = "O"
    
    def move(self, direction):
        
        sourcePos = self.pos
        
        #"EWWWW"
        def addDirection(a, b):
            return tuple([sum(x) for x in zip(a,b)])
        
        if direction == Direction.up:
            destPos = addDirection(sourcePos, (0, -1))
        
        if direction == Direction.left:
            destPos = addDirection(sourcePos, (-1, 0))
        
        if direction == Direction.down:
            destPos = addDirection(sourcePos, (0, 1))
        
        if direction == Direction.right:
            destPos = addDirection(sourcePos, (1, 0))
            
        if self.board.isValidPos(destPos):
            self.board.moveSquare(sourcePos, destPos)
        
    
class Food(aPiece):
    char = "%"