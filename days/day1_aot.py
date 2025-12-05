import sys

def convert(s: str) -> int:
    return -int(s[1:]) if s[0] == "L" else int(s[1:])

def part1(turns):
    dial = 50
    modu = 100
    answ = 0
    for turn in turns:
        dial = (dial + turn) % modu
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
            answ += (modu - dial - turn) // modu - (dial == 0)

        dial = (dial + turn) % modu
    print(answ)

data = sys.stdin.read()
data = data.splitlines()
turns = [ convert(line) for line in data ]
part1(turns)
part2(turns)


