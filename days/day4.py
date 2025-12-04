import sys

def check_adjacent(posi_num, line_num, dep):
    rolls = 0
    for i in range(posi_num - 1, posi_num + 2):
        if i < 0:
            continue
        if i >= len(dep[line_num]):
            continue
        for j in range(line_num - 1, line_num + 2):
            if j < 0:
                continue
            if j >= len(dep):
                continue
            if i == posi_num and j == line_num:
                continue
            if dep[j][i] == '@':
                rolls += 1
    return rolls



def part1(dep):
    possible = 0
    for line_num, line in enumerate(dep):
        for posi_num, posi in enumerate(line):
            if posi == '.':
                continue
            adjacent = check_adjacent(posi_num, line_num, dep)
            if adjacent < 4:
                possible += 1
    print(possible)


def part2(dep):
    removed = 0
    while True:
        possible = 0
        for line_num, line in enumerate(dep):
            for posi_num, posi in enumerate(line):
                if posi != '@':
                    continue
                adjacent = check_adjacent(posi_num, line_num, dep)
                if adjacent < 4:
                    possible += 1
                    dep[line_num][posi_num] = 'x'
                    # print(line_num, posi_num, adjacent)
            #print(line)
        if possible == 0:
            break
        #print(possible)
        removed += possible
    print(removed)

data = sys.stdin.read().splitlines()
department = [list(d) for d in data]

part1(data)
part2(department)



