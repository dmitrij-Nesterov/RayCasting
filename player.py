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

    def movement(self, fps):
        keys = pg.key.get_pressed()
        speed = player_speed / fps
        delta_angle = player_delta_angle / fps
        cos_a = math.cos(self.angle)
        sin_a = math.sin(self.angle)
        if keys[pg.K_LSHIFT]:
            speed *= 2
        if keys[pg.K_w]:
            self.x += speed * cos_a
            self.y += speed * sin_a
        if keys[pg.K_s]:
            self.x -= speed * cos_a
            self.y -= speed * sin_a
        if keys[pg.K_a]:
            self.x += speed * sin_a
            self.y -= speed * cos_a
        if keys[pg.K_d]:
            self.x -= speed * sin_a
            self.y += speed * cos_a
        if keys[pg.K_LEFT]:
            self.angle -= delta_angle
        if keys[pg.K_RIGHT]:
            self.angle += delta_angle
