import sys

data = sys.stdin.read().splitlines()
racks = {}
outs = {}

for line in data:
    split_line = line.replace(':', '').split(' ')
    key = split_line[0]
    racks[key] = []
    for server in split_line[1:]:
        if server == 'out':
            outs[key] = 1
            break
        racks[key].append(server)


visited = []
tbd = [o for o in outs]

while tbd:
    key = tbd.pop()
    for server in racks:
        if key in racks[server]:
            racks[server].remove(key)
            if len(racks[server]) == 0:
                tbd.append(server)
            if server not in outs:
                 outs[server] = 0
            outs[server] += outs[key]

outs['you']