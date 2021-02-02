# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:33:00 2021

@author: dromp_50a1bpc
"""
import enum


class Player:
    def __init__(self, name, board):
        self.name = name
        self.board = board
        self.tiles = []
        self.color_set_size = {}
        
    def add_tile(self, tile):
        self.tiles.append(tile)
        self.add_to_color_set_size(tile.color)
        
    def add_to_color_set_size(self, color):
        try:
            self.color_set_size[color.values()] += 1
        except:
            self.color_set_size[color.values()] = 1
        
    def has_color_set(self, color):
        try:
            if self.color_set_size[color.values()] == self.board.color_set_size[color.values()]: return True
            return False
        except:    
            return False
        
    def get_all_color_sets(self):
        matches = []
        for color_values in self.color_set_size:
            color = Color(color_values)
            if self.has_color_set(color): matches.append(color)
        return matches


class Board:
    def __init__(self):
        self.tiles = []
        self.color_set_size = {}
        self.players = []
        
    def add_tile(self, tile):
        self.tiles.append(tile)
        self.add_to_color_set_size(tile.color)
        
    def add_to_color_set_size(self, color):
        try:
            self.color_set_size[color.values()] += 1
        except:
            self.color_set_size[color.values()] = 1

    def add_player(self, player):
        self.players.append(player)


class Tile:
    def __init__(self, name, tile_type, rent, tile_pos, tile_img, color, tile_size):
        self.name = name
        self.tile_type = tile_type
        self.tile_pos = tile_pos
        self.rent = rent
        self.tile_img = tile_img
        self.color = color
        self.tile_size = tile_size
      
    #def get_rent(self, player = "", roll = 0):
       # if(roll == 0): 

class Rent:
    def __init__(self, rent_price, house_price, hotel_price, cur_houses = 0, player_discounts = {}):
        self.rent_price = rent_price
        self.player_discounts = player_discounts.copy()
        self.house_price = house_price
        self.hotel_price = hotel_price
        self.cur_houses = cur_houses 

    def add_player_discount(self, player, discount):
        try: self.player_discounts[player] += discount
        except: self.player_discounts[player] = discount

    def get_player_discount(self, player):
        try: return self.player_discounts[player]
        except: return 0


class TileType(enum.Enum):
    PROPERTY = 0,
    RAILROAD = 1,
    UTILITY = 2,
    TAX = 3,
    COLLECT = 4,
    CHANCE = 5,
    COMMUNITY_CHEST = 6,
    JAIL = 7


    
class Color:
    def __init__(self, RGB = (0,0,0)):
        self.R = min(255, max(RGB[0], 0))
        self.G = min(255, max(RGB[1], 0))
        self.B = min(255, max(RGB[2], 0))
        
    def same_as(self, other):
        return (other.R == self.R and other.G == self.G and other.B == self.B)
    
    def values(self):
        return (self.R, self.G, self.B)

class Size():
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def scale(self, scale):
        self.X *= scale
        self.Y *= scale