'''
Created on Aug 17, 2016

@author: TDARSEY
'''


class Square:
    
    EMPTYCHAR = "-"
    
    def __init__(self, contents = None):
        self.contents = contents
        
    def __str__(self):
        
        returnString = self.EMPTYCHAR
        
        if(self.contents):
            returnString = self.contents
            
        return returnString + " "



class Board:
    def __init__(self, size=(16, 16)):
        assert(len(size) == 2)
        
        self.squares = []
        
        row = [ Square() ] * size[1]

        for i in range(size[0]):
            self.squares.append(deepcopy(row))
       
    def __getitem__(self, index):
        return self.squares.__getitem__(index)
    
    """
    def __setitem__(self, index, value):
        self.squares[index] = Square(value)
    """
    def setSquare(self, pos, value):
        self.squares[pos[1]][pos[0]] = Square(value)
    
    
    def __str__(self):
        
        returnString = ""
        
        for row in self.squares:
            for square in row:
                returnString += str(square)
                
            returnString += "\n"
            
        return returnString


     
if __name__ == "__main__":
 
    from copy import deepcopy
    import os
    
    clear = lambda: os.system('cls')
 
    myBoard = Board()
    
    myBoard.setSquare((5, 1), "X")
    print myBoard
    clear()