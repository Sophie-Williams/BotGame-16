'''
Created on Aug 25, 2016

@author: TDARSEY
'''

import logging

from enum import Direction

import random

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)

logger = logging.getLogger('botgames')

class aPiece(object):
    char = '?'
    consumable = False
    def __init__(self, board = None, pos = None):
        self.board = board
        self.pos = pos
    
    def __str__(self):
        return self.char
    

    
class Block(aPiece):
    char = "X"
    
class Bot(aPiece):
    char = "O"
    
    def __init__(self):
        self.health = 1
    
    def move(self, direction):
        
        sourcePos = self.pos

        if direction == Direction.up:
            self._moveOffset(sourcePos, (0, -1))
        
        if direction == Direction.left:
            self._moveOffset(sourcePos, (-1, 0))
        
        if direction == Direction.down:
            self._moveOffset(sourcePos, (0, 1))
        
        if direction == Direction.right:
            self._moveOffset(sourcePos, (1, 0))


    def _moveOffset(self, sourcePos, offset):
        destPos = tuple([sum(x) for x in zip(sourcePos,offset)])

      

        if self.board.isValidPos(destPos):
            
            #Eat
            if(self.board 
                and self.board.getSquare(destPos) 
                and self.board.getSquare(destPos).__class__.__name__ == "Food"
               ):
                food = self.board.getSquare(destPos)
                self._eat(food)
            
            #Move
            self.board.moveSquare(sourcePos, destPos)  
        else:
            pass
            #logger.warning('Attempted invalid move: %s to %s.', sourcePos, destPos)    
    
    def onConsume(self):
        self.health += 100
    
    def tick(self):
        self.health -= 0.01
        if(self.health <= 0):
            if(self.board):
                self.board.clearSquare(self.pos)
            del self
        else:
            self.onTick()
        
    
        #Override
    def onTick(self):
        pass
    
    def _eat(self, food):
        self.health += 1
    
    
class RandoBot(Bot):
    def onTick(self):

        directions = [
            Direction.up,
            Direction.down, 
            Direction.left, 
            Direction.right]

        self.move(random.choice(directions))

class Food(aPiece):
    char = "%"
    consumable = True