import pygame as pg
from drawing import Drawing
from settings import *
from player import Player
from map import world_map
from ray_casting import ray_casting
import math

pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
player = Player()
drawing = Drawing(sc)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)

    # pg.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    # pg.draw.line(sc, GREEN, (int(player.x), int(player.y)), (player.x + WIDTH * math.cos(player.angle),
    #                                              player.y + HEIGHT * math.sin(player.angle)))
    # for x, y in world_map:
    #     pg.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)

    pg.display.flip()
    clock.tick()