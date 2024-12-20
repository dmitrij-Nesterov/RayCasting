import math
import pygame as pg
from settings import *
from map import world_map

def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE

def ray_casting(sc, player_pos, player_angel):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angel - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # verticals
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE):
            depth_v = (x - ox) / cos_a
            y = oy + depth_v * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * TILE

        # horizontals
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, WIDTH, TILE):
            depth_h = (y - oy) / sin_a
            x = ox + depth_h * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * TILE

        #projection
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angel - cur_angle)
        proj_height = PROJ_COEFF / max(depth, 0.00001)
        c = 255 // (1 + depth * depth * 0.00001)
        pg.draw.rect(sc, (c, c // 2, c // 3), (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
        cur_angle += DELTA_ANGLE
