import sys

def optimize_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    new_ranges = [ranges[0]]
    for start, end in ranges[1:]:
        if start <= new_ranges[-1][1]:
            new_ranges[-1][1] = max(new_ranges[-1][1], end)
        else:
            new_ranges.append([start, end])
    return new_ranges

def part1(ranges, ingredients):
    fresh = 0
    for i in ingredients:
        for r in ranges:
            if i in range(r[0], r[1]):
                fresh += 1
                break
    print(fresh)

def part2(ranges):
    unique = 0
    for r in ranges:
        unique += len(range(r[0], r[1]))
    print(unique)


data = sys.stdin.read().split('\n\n')
ranges = optimize_ranges([[int(r.split('-')[0]), int(r.split('-')[1]) + 1] for r in data[0].splitlines()])
ingredients = [int(d) for d in data[1].splitlines()]
part1(ranges, ingredients)
part2(ranges)



