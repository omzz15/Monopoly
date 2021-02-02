# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:33:00 2021

@author: dromp_50a1bpc
"""
import enum
import random
import Monopoly_Data as MD


board = MD.Board()
player1 = MD.Player("P1", board)
player2 = MD.Player("P2", board)

colors = []
for i in range(10):
    colors.append(MD.Color((random.randint(0,256),random.randint(0,256),random.randint(0,256))))

for i in range(10):
    tile = MD.Tile(None,None,None,None,None,colors[random.randint(0,len(colors) - 1)], None)
    board.add_tile(tile)
    if random.randint(0, 1):
        player1.add_tile(tile)
    else:
        player2.add_tile(tile)
        
print(player1.get_all_color_sets())
print("")
print(player2.get_all_color_sets())
