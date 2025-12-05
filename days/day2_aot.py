import sys

def part1(ids):
    sum = 0
    for id in ids:
        id_len = len(id)
        if id[:id_len//2] == id[id_len//2:]:
            sum += int(id)
    print(sum)

def part2(ids):
    sum = 0
    for id in ids:
        if id in (id + id)[1:-1]:
            sum += int(id)
    print(sum)

data = sys.stdin.read().replace("-", ",").split(",")
ranges = [str(num) for iter in range(0, len(data), 2) for num in range(int(data[iter]), int(data[iter+1]) + 1)]

part1(ranges)
part2(ranges)


