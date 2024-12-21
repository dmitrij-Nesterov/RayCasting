from settings import *
import pygame as pg

text_map = [
    '1111111111111131111111111111111',
    '1........1.....1..........1...1',
    '1.................1...1.......1',
    '1..........1...1......11.....1',
    '1.......1..............1......1',
    '1.......1......1.....1........1',
    '1111..111111...1...1111111..111',
    '1.......11...........11.......1',
    '1.......11....2.2....11.......1',
    '111.........................111',
    '1.......11....2.2....11.......1',
    '1.......11...........11.......1',
    '1111..113111...1...111111..1111',
    '1.1............1........1.....1',
    '1.......1...........1......1..1',
    '1..1...........1......1...11..1',
    '1.11...1...........1......1...1',
    '1.........1....1........1.....3',
    '1111111111111111111111111111111'
]
collision_walls = []
world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            collision_walls.append(pg.Rect(i * TILE, j * TILE, TILE, TILE))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            world_map[(i * TILE, j * TILE)] = char