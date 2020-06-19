from random import random

from pygame.math import Vector2

from logic import Game, Player

def level_1():
    g = Game()
    g.add_player(Player(position=Vector2(0.2, 0.5),
                        movement=Vector2(0, 0.002*random())))
    g.add_player(Player(position=Vector2(0.8, 0.5),
                        movement=Vector2(0, 0.002*random())))
    return g
