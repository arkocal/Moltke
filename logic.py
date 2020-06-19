import pygame

class Player:
    def __init__(self, position, movement):
        self.position = position
        self.movement = movement

    def turn_cw(self):
        self.movement.rotate(90)

    def turn_ccw(self):
        self.movement.rotate(-90)

class Game:
    def __init__(self):
        self.player_count = 2
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def tick(self):
        for p in self.players:
            p.position += p.movement

    def turn_cw()
        for p in self.players:
            p.turn_cw()

    def turn_ccw()
        for p in self.players:
            p.turn_cw()
        
