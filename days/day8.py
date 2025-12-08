import sys

def get_nearest_point(point_id, coords):
    nearest_hund = []
    for id, coord in enumerate(coords):
        if id == point_id:
            continue
        dist = ((coord[0] - coords[point_id][0]) ** 2
                + (coord[1] - coords[point_id][1]) ** 2
                + (coord[2] - coords[point_id][2]) ** 2)
        if len(nearest_hund) < 4:
            nearest_hund.append((dist,point_id, id))
            nearest_hund = sorted(nearest_hund, key=lambda x: x[0])
            continue
        if dist < nearest_hund[-1][0]:
            nearest_hund.pop(-1)
            nearest_hund.append((dist, point_id, id))
            nearest_hund = sorted(nearest_hund, key=lambda x: x[0])
    return nearest_hund

def treestuff(pairs):
    circuits = []
    for p_id, pair in enumerate(pairs):
        hits = []
        for circuit_id, circuit in enumerate(circuits):
            if pair[1] in circuit or pair[2] in circuit:
                circuit.add(pair[1])
                circuit.add(pair[2])
                hits.append(circuit_id)
        if not len(hits):
            new_circuit = set()
            new_circuit.add(pair[1])
            new_circuit.add(pair[2])
            circuits.append(new_circuit)
        if len(hits) > 1:
            for hit in hits[1:]:
                circuits[hits[0]].update(circuits.pop(hit))
        if p_id == 999:
            part1 = 1
            for circuit in sorted(circuits, key=lambda p: len(p))[-3:]:
                part1 *= len(circuit)
            print(part1)
        if len(circuits) == 1 and len(circuits[0]) == 1000:
            return pair[1], pair[2]


data = sys.stdin.read().splitlines()
coords = [[int(num) for num in line.split(',')] for line in data]
pairs = []
for point_id, point in enumerate(coords):
    pairs.extend(get_nearest_point(point_id, coords))

pairs = sorted(pairs, key=lambda p: p[0])

for p_id, pair in enumerate(pairs):
    if (pair[0], pair[2], pair[1]) in pairs:
        pairs.pop(p_id)

box1, box2 = treestuff(pairs)
print(coords[box1][0] * coords[box2][0])





