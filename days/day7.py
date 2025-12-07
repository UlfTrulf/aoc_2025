import sys

from gi.overrides.keysyms import value


def get_start(line):
    for c, char in enumerate(line):
        if char == 'S':
            return c, 0
    return None


#def part1_alt(data, start):
#    col = {}
#    col.add(start[0])
#    splits = 0
#    for row, line in enumerate(data[1:-1]):
#        next_col = set()
#        for c in col:
#            if c < 0 or c >= len(data):
#                continue
#            if data[row + 1][c] == '^':
#                next_col.add(c + 1)
#                next_col.add(c - 1)
#                splits += 1
#            else:
#                next_col.add(c)
#            col = next_col
#    print(splits)

#def part1(data, start):
#    points = set()
#    points.add(start)
#    splits = 0
#    while len(points) > 0:
#        next_points = set()
#        for p in points:
#            if p[1] >= len(data) - 1 or p[0] < 0 or p[0] >= len(data[0]):
#                continue
#            if data[p[1] + 1][p[0]] == '^':
#                next_points.add((p[0] + 1, p[1] + 1))
#                next_points.add((p[0] - 1, p[1] + 1))
#                splits += 1
#            else:
#                next_points.add((p[0], p[1] + 1))
#        points = next_points
#
#    print(splits)


def maps(data, start):
    dimensions = {}
    points = set()
    points.add(start)
    dimensions[start] = 1
    splits = 0
    while len(points) > 0:
        next_points = set()
        for p in points:
            dim = dimensions.get(p)
            if p[1] >= len(data) - 1 or p[0] < 0 or p[0] >= len(data[0]):
                continue
            if data[p[1] + 1][p[0]] == '^':
                next_points.add((p[0] + 1, p[1] + 1))
                next_points.add((p[0] - 1, p[1] + 1))
                dimensions.setdefault((p[0] + 1, p[1] + 1), 0)
                dimensions.setdefault((p[0] - 1, p[1] + 1), 0)
                dimensions[(p[0] + 1, p[1] + 1)] += dim
                dimensions[(p[0] - 1, p[1] + 1)] += dim
                splits += 1
            else:
                next_points.add((p[0], p[1] + 1))
                dimensions.setdefault((p[0], p[1] + 1), 0)
                dimensions[(p[0], p[1] + 1)] += dim
        points = next_points
    end = {
        key: value
        for key, value in dimensions.items()
        if key[1] == len(data) - 1
    }
    print(splits)
    print(sum(end.values()))

data = sys.stdin.read().splitlines()
start = get_start(data[0])
maps(data, start)