'''
Created on Aug 17, 2016

@author: TDARSEY
'''
from copy import deepcopy
    
from piece import Block, Bot

from enum import Direction

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
        self.squares[pos[1]][pos[0]] = piece
        piece.pos = pos
        piece.board = self
        
    def clearSquare(self, pos):
        piece = self.squares[pos[1]][pos[0]]
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
        if(     pos[0] >= 0 
           and  pos[0] < self._size[0]
           and  pos[1] >= 0 
           and  pos[1] < self._size[1]):
            return True
        return False
    
    def __str__(self):
        
        spacer = " "
        emptychar = '-'
        
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
