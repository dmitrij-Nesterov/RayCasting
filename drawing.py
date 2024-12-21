import pygame as pg
from settings import *
from ray_casting import ray_casting
from map import mini_map

class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pg.font.SysFont('Arial', 36, bold=True)
        self.texture = pg.image.load("img/1.png").convert()

    def background(self):
        pg.draw.rect(self.sc, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pg.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle, self.texture)

    def fps(self, fps):
        display_fps = str(int(fps))
        render = self.font.render(display_fps, 0, RED)
        self.sc.blit(render, FPS_POS)

    def mini_map(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pg.draw.line(self.sc_map, GREEN, (map_x, map_y), (map_x + 10 * math.cos(player.angle),
                                                                 map_y + 10 * math.sin(player.angle)))
        pg.draw.circle(self.sc_map, GREEN, (int(map_x), int(map_y)), 5)

        for x, y in mini_map:
            pg.draw.rect(self.sc_map, GREEN_BLACK, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)