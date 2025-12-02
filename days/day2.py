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

data = sys.stdin.read()
data = data.replace("-", ",")
numbers = data.split(",")
ranges = []
iter = 0
while iter < len(numbers) - 1:
    start = int(numbers[iter])
    end = int(numbers[iter + 1])
    num = start
    while num <= end:
        ranges.append(str(num))
        num += 1
    iter += 2

part1(ranges)
part2(ranges)


