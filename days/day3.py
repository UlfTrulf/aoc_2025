import sys
import numpy as np

def do_stuff(batteries, turn_ons):
    number = 0
    last_max = -1
    while turn_ons > 0:
        search = batteries[last_max + 1:len(batteries) - turn_ons + 1]
        cur_max = np.argmax(search)
        turn_ons -= 1
        number += (10 ** turn_ons) * search[cur_max]
        last_max = cur_max + 1 + last_max
    return number

def part1(bench):
    sum = 0
    on = 2
    for b in bench:
        sum += do_stuff(b, on)
    print(sum)

def part2(bench):
    sum = 0
    on = 12
    for b in bench:
        sum += do_stuff(b, on)
    print(sum)

data = sys.stdin.read()
data = data.splitlines()
bench = []
for line in data:
    bench.append(list(map(int, line)))
part1(bench)
part2(bench)


