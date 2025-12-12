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
        racks[key].append(server)


ffts = {}
dacs = {}
tbd = []
for o in outs:
    tbd.append(o)
    dacs[o] = int(o == 'dac')
    ffts[o] = int(o == 'fft')
dacs['dac'] = 1
ffts['fft'] = 1
while tbd:
    key = tbd.pop()
    for server in racks:
        if key in racks[server]:
            racks[server].remove(key)
            if len(racks[server]) == 0:
                tbd.append(server)
            if server not in ffts:
                ffts[server] = 0
            if server not in dacs:
                dacs[server] = 0
            if server not in outs:
                 outs[server] = 0
            outs[server] += outs[key]
            ffts[server] += ffts[key]
            dacs[server] += dacs[key]
print(outs['you'])
print(dacs['svr'] * ffts['dac'] * outs['fft'] + ffts['svr'] * dacs['fft'] * outs['dac'])

