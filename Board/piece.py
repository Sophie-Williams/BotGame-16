'''
Created on Aug 25, 2016

@author: TDARSEY
'''

import logging

from enum import Direction


FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)

logger = logging.getLogger('botgames')

logger.warning('Loading: %s', 'Pieces')

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


        if direction == Direction.up:
            destPos = self.moveOffset(sourcePos, (0, -1))
        
        if direction == Direction.left:
            destPos = self.moveOffset(sourcePos, (-1, 0))
        
        if direction == Direction.down:
            destPos = self.moveOffset(sourcePos, (0, 1))
        
        if direction == Direction.right:
            destPos = self.moveOffset(sourcePos, (1, 0))
            

  

    def moveOffset(self, sourcePos, offset):
        destPos = tuple([sum(x) for x in zip(sourcePos,offset)])



        if self.board.isValidPos(destPos):
            logger.warning(destPos)
            self.board.moveSquare(sourcePos, destPos)  
        else:
            logger.warning('Attempted invalid move: %s to %s.', sourcePos, destPos)    
    
class Food(aPiece):
    char = "%"