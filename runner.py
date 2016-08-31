'''
Created on Aug 23, 2016

@author: TDARSEY
'''
from Board.piece import RandoBot
from GameWorld.gameworld import GameWorld

gw = GameWorld()
gw.addBot(RandoBot())
gw.addBot(RandoBot())
gw.run()