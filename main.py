import pygame as pg
from drawing import Drawing
from settings import *
from player import Player
from map import world_map
from ray_casting import ray_casting
import math

pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
sc_map = pg.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pg.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)

while True:
    fps = max(clock.get_fps(), 0.00001)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    player.movement(fps)
    sc.fill(BLACK)

    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(fps)
    # drawing.mini_map(player)

    pg.display.flip()
    clock.tick()