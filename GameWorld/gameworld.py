'''
Created on Aug 23, 2016

@author: TDARSEY
'''

import util

from Board.board import Board
from Board.piece import Bot, Food, RandoBot
from Board.enum import Direction
import random


class GameWorld:
    
    def __init__(self):
        self.clock = 0
        self.flipint = 1
        self.board = Board()
        self.bots = []
    
    def flip(self):
        util.clear()
        print self.board
        
    def tick(self):
        
        self.clock += 1
        
        if(random.randint(0, 100) == 50):
            self.board.setSquare((
                   random.randint(0, self.board._size[0] - 1), 
                   random.randint(0, self.board._size[1] - 1)), 
                Food())
        
        for bot in self.bots:
            bot.onTick()
        
        #if(not myBot.board):
        #    exit()
    
    def addBot(self, bot, pos=None):
        
        if not pos:
            pos = self.board.getRandomValidPosition()
        
        self.bots.append(bot)
        self.board.setSquare(pos, bot)
    
    def run(self):
        while(True):
            
            self.tick()
        
            if(self.clock % self.flipint == 0):
                self.flip()

if __name__ == "__main__":
    gw = GameWorld()
    gw.addBot(RandoBot())
    gw.addBot(RandoBot())
    gw.run()


    #time.sleep(0.03)