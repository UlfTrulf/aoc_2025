import sys
from shapely.geometry import Polygon
from collections import defaultdict

data = sys.stdin.read().splitlines()
red_tiles = [[int(num) for num in line.split(',')] for line in data]
largest_rect = 0
adj = defaultdict(list)

for tileA_index in range(len(red_tiles)):
    tileA = red_tiles[tileA_index]
    for tileB_index in range(tileA_index + 1, len(red_tiles)):
        tileB = red_tiles[tileB_index]
        min_x = min(tileA[0], tileB[0])
        max_x = max(tileA[0], tileB[0])
        min_y = min(tileA[1], tileB[1])
        max_y = max(tileA[1], tileB[1])
        rect = (max_x - min_x + 1) * (max_y - min_y + 1)

        if tileA[0] == tileB[0] or tileA[1] == tileB[1]:
            adj[tileA_index].append(tileB_index)
            adj[tileB_index].append(tileA_index)

        if rect > largest_rect:

            for test_tile_index in range(len(red_tiles)):
                if test_tile_index == tileA_index or test_tile_index == tileB_index:
                    continue

                test_tile = red_tiles[test_tile_index]

                if min_x < test_tile[0] < max_x and min_y < test_tile[1] < max_y:
                    continue
                largest_rect = rect

print(largest_rect)

loops = []

def search_poly(start, current, path):
    if current == start and len(path) > 2:
        loops.append(path)
        return

    if current in path and current != start:
        return

    path.append(current)

    for neighbor in adj.get(current, []):
        if neighbor != start and neighbor in path:
            continue

        if len(path) > 1 and neighbor == path[-2]:
            continue

        if neighbor == start and len(path) >= 2:
            search_poly(start, neighbor, path)
        elif neighbor != start:
            search_poly(start, neighbor, path)


for tile_index in range(len(red_tiles)):
    search_poly(tile_index, tile_index, [])

unique_loops = []
unique_loop_indeces = []

for loopA, l_a in enumerate(loops):
    if set(l_a) not in unique_loops:
        unique_loops.append(set(l_a))
        unique_loop_indeces.append(loopA)

polygons = []
for loop_index in unique_loop_indeces:
    corners = [red_tiles[tile_index] for tile_index in loops[loop_index]]
    polygons.append(Polygon(corners))

largest_rect = 0

for tileA_index in range(len(red_tiles)):
    tileA = red_tiles[tileA_index]
    for tileB_index in range(tileA_index + 1, len(red_tiles)):
        tileB = red_tiles[tileB_index]
        min_x = min(tileA[0], tileB[0])
        max_x = max(tileA[0], tileB[0])
        min_y = min(tileA[1], tileB[1])
        max_y = max(tileA[1], tileB[1])
        area = (max_x - min_x + 1) * (max_y - min_y + 1)
        rect = Polygon([(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)])
        if area > largest_rect:
            for poly in polygons:
                if rect.within(poly):
                    largest_rect = area

print(largest_rect)

