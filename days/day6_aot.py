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
    transposed = list(zip(*data))
    answer = 0
    iter = 0
    line = []
    for number in transposed:
        try:
            num = int(''.join(number).strip())
            line.append(num)
        except ValueError:
            answer += calc(commands[iter], line)
            iter += 1
            line = []
    answer += calc(commands[iter], line)
    print(answer)


data = sys.stdin.read().splitlines()
commands = data[-1].split()
part1(commands, data)
part2(commands, data[:-1])


