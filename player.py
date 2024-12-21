from settings import *
import pygame as pg
import math
from map import collision_walls

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        # collision parameters
        self.side = 50
        self.rect = pg.Rect(*player_pos, self.side, self.side)

    @property
    def pos(self):
        return self.x, self.y

    def detect_collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(collision_walls)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = collision_walls[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

                if abs(delta_x - delta_y) < 10:
                    dx, dy = 0, 0
                elif delta_x > delta_y:
                    dy = 0
                elif delta_y > delta_x:
                    dx = 0
        self.x += dx
        self.y += dy

    def movement(self, fps):
        keys = pg.key.get_pressed()
        speed = player_speed / fps
        delta_angle = player_delta_angle / fps
        cos_a = math.cos(self.angle)
        sin_a = math.sin(self.angle)
        dx, dy = 0, 0
        if keys[pg.K_LSHIFT]:
            speed *= 2
        if keys[pg.K_w]:
            dx += speed * cos_a
            dy += speed * sin_a
        if keys[pg.K_s]:
            dx -= speed * cos_a
            dy -= speed * sin_a
        if keys[pg.K_a]:
            dx += speed * sin_a
            dy -= speed * cos_a
        if keys[pg.K_d]:
            dx -= speed * sin_a
            dy += speed * cos_a
        if keys[pg.K_LEFT]:
            self.angle -= delta_angle
        if keys[pg.K_RIGHT]:
            self.angle += delta_angle
        self.detect_collision(dx, dy)
        self.rect.center = self.x, self.y