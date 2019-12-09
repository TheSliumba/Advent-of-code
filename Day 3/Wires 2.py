def setup_instructions(file):
    for line in file:
        line = line.strip()
        if line:
            instructions = [(w[0], int(w[1:])) for w in line.split(',')]
            yield instructions

def calculate_all_coords(instructions):
    position = [0,0]
    coordinates = {}
    steps = 0
    for direction, distance in instructions:
        for _ in range(distance):
            if direction == "R":
                position[0] += 1
            if direction == "L":
                position[0] -= 1
            if direction == "D":
                position[1] -= 1
            if direction == "U":
                position[1] += 1
            steps += 1
            pos = tuple(position)
            coordinates[pos] = coordinates.get(pos, steps)
    return coordinates

with open("Input.txt") as f:
    reader = setup_instructions(f)
    fst_ln_inst = next(reader)
    snd_ln_inst = next(reader)

    first_coords = calculate_all_coords(fst_ln_inst)
    second_coords = calculate_all_coords(snd_ln_inst)
    common_coords = set(first_coords).intersection(set(second_coords))
    all_sums = sorted([first_coords[k] + second_coords[k] for k in common_coords])
    print(all_sums[0])