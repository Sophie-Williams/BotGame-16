'''
Created on Aug 17, 2016

@author: TDARSEY
'''

import logging

from copy import deepcopy
    
from piece import Block, Food, Bot

from enum import Direction

logger = logging.getLogger('botgames')

class Board:
    def __init__(self, size=(16, 16)):
        self.clearToSize(size) 
        
    def clearToSize(self, size):
        assert(len(size) == 2)
        self._size = size
        
        self.squares = []
        
        row = [ None ] * size[1]

        for i in range(size[0]):
            self.squares.append(deepcopy(row))
       
    def __getitem__(self, index):
        return self.squares.__getitem__(index)
    
    def getSquare(self, pos):
        return self.squares[pos[1]][pos[0]]
    
    def setSquare(self, pos, piece):
        if(self.isValidPos(pos)):
            piece.pos = pos
            piece.board = self
            self.squares[pos[1]][pos[0]] = piece
            #logger.error('Spawned %s at %s', repr(piece), pos)
        else:
            logger.error('Attempt to set invalid square : %s at %s', repr(piece), pos)
            exit()
            
    def clearSquare(self, pos):
        piece = self.squares[pos[1]][pos[0]]
        if piece:
            piece.pos = None
            piece.board = None
        self.squares[pos[1]][pos[0]] = None
        
    def moveSquare(self, sourcePos, destPos):
        piece = self.getSquare(sourcePos)
        if not piece:
            return

        self.clearSquare(sourcePos)
        self.setSquare(destPos, piece)
    
    def isValidPos(self, pos):
        
        #Invalid if out of the board's range
        if(    pos[0] <  0 
           or  pos[0] >= self._size[0]
           or  pos[1] <  0 
           or  pos[1] >= self._size[1]):
            #logger.warning('Invalid pos: %s to %s', self, pos)
            return False
        
        #Invalid if a nonconsumable piece is present
        currentPieceIfAny = self.getSquare(pos)
        if currentPieceIfAny and (not currentPieceIfAny.consumable):
            #logger.warning('Invalid pos - Occupied Square: %s to %s', self, pos)
            return False
        
        #Valid
        return True
    
    def __str__(self):
        
        spacer = " "
        emptychar = ' '
        
        returnString = ""
        
        for row in self.squares:
            
            returnString += "|" + spacer
            for square in row:
                returnString += str(square) if square else emptychar
                returnString += spacer
            returnString += "|"
            returnString += "\n"
            
        return returnString


if __name__ == "__main__":
 
    myBoard = Board((4, 4))
    myBot = Bot()
    myBoard.setSquare((1, 1), myBot)
    
    #myBoard.moveSquare((1, 1), (1, 2))
    myBot.move(Direction.up)
    
    print myBoard
