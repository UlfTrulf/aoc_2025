import sys

def calc(command, nums):
    if command == "+":
        return sum(nums)
    mult = 1
    for num in nums:
        mult = mult * num
    return mult

def part1(commands, data):
    matrix = [[int(line.split()[i]) for line in data[:-1]] for i in range(len(data[0].split()))]
    answer = 0
    for iter, command in enumerate(commands):
        answer += calc(command, matrix[iter])
    print(answer)

def part2(commands, data):
    numbers = '|'.join([''.join([list(line)[i].strip() for line in data[:-1]]) for i in range(len(list(data[0])))]).split('||')
    answer = 0
    for iter, command in enumerate(commands):
        answer += calc(command, [int(num) for num in numbers[iter].split('|')])
    print(answer)


data = sys.stdin.read().splitlines()
commands = data[-1].split()
part1(commands, data)
part2(commands, data)


