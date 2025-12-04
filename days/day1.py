import sys

def convert(s: str, n: int) -> int:
    if s == "L":
        return -n
    else:
        return n

def part1(turns):
    dial = 50
    modu = 100
    answ = 0
    for turn in turns:
        dial = dial + turn
        dial = dial % modu
        if dial == 0:
            answ += 1
    print(answ)

def part2(turns):
    dial = 50
    modu = 100
    answ = 0
    for turn in turns:
        if turn > 0:
            answ += (dial + turn) // modu
        else:
            answ += (modu - dial - turn) // modu
            if dial == 0:
                answ -= 1

        dial = (dial + turn) % modu
    print(answ)

data = sys.stdin.read()
data = data.splitlines()
turns = [ convert(line[0], int(line[1:])) for line in data ]
part1(turns)
part2(turns)


