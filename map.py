from settings import *

text_map = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'W........W.....W..........W...W',
    'W...W.............W...W.......W',
    'W..WW......W...W......WW.....W',
    'W......W...............W......W',
    'W.......W......W.....W........W',
    'WWWW..WWWWWW...W...WWWWWWW..WWW',
    'W.......WW...........WW.......W',
    'W.......WW....W.W....WW.......W',
    'WWW.........................WWW',
    'W.......WW....W.W....WW.......W',
    'W.......WW...........WW.......W',
    'WWWW..WWWWWW...W...WWWWWW..WWWW',
    'W.W............W........W.....W',
    'W.......W...........W......W..W',
    'W..W...........W......W...WW..W',
    'W.WW...W...........W......W...W',
    'W.........W....W........W.....W',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
]

world_map = set()
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
