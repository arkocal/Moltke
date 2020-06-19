import pygame
from pygame.locals import *

import levels

pygame.init()
WIDTH = 1000
HEIGHT = 1000

class GameDisplay:

    def __init__(self):
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))

    @property
    def size(self):
        return self.surface.get_width()

    def absolute(self, *cos):
        if len(cos) == 1:
            return int(cos[0]*self.size)
        return tuple(int(c*self.size) for c in cos)

    def draw_object(self, obj):
        color = pygame.Color(255, 255, 0)
        rect = self.absolute(*obj.top_left, *obj.box)
        pygame.draw.rect(self.surface, color, rect)

    def draw_game(self, game):
        self.surface.fill(pygame.Color(0, 0, 0))
        for player in game.players:
            self.draw_object(player)


import math, time
def game_loop():
    i = 0
    game = levels.level_1()
    display = GameDisplay()
    while True:
        pygame.display.update()
        i += 0.01
        time.sleep(0.01)
        game.tick()
        display.draw_game(game)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    game.turn_cw()
                if event.key == pygame.K_s:
                    game.turn_ccw()
            if event.type == QUIT:
                pygame.quit()
                break

game_loop()
