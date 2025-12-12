import sys

data = sys.stdin.read().split('\n\n')

trees = data[-1]
part1 = 0
for tree in trees.splitlines():
    line = tree.split(':')
    dim = [int(l) for l in line[0].split('x')]
    presents = [int(p) for p in line[1].strip().split(' ')]
    part1 += int(dim[0]* dim[1] > sum(presents) * 7)
print(part1)
print()