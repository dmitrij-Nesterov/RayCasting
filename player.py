from settings import *
import pygame as pg
import math

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return self.x, self.y

    def movement(self):
        keys = pg.key.get_pressed()
        cos_a = math.cos(self.angle)
        sin_a = math.sin(self.angle)
        if keys[pg.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pg.K_s]:
            self.x -= player_speed * cos_a
            self.y -= player_speed * sin_a
        if keys[pg.K_a]:
            self.x += player_speed * sin_a
            self.y -= player_speed * cos_a
        if keys[pg.K_d]:
            self.x -= player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pg.K_LEFT]:
            self.angle -= 0.02
        if keys[pg.K_RIGHT]:
            self.angle += 0.02
