def setup_instructions(file):
    for line in file:
        line = line.strip()
        if line:
            instructions = [(w[0], int(w[1:])) for w in line.split(',')]
            yield instructions

def calculate_all_coords(instructions):
    position = [0,0]
    coordinates = set()
    for direction, distance in instructions:
        if direction == "R":
            for _ in range(distance):
                position[0] += 1
                coordinates.add(tuple(position))
        if direction == "L":
            for _ in range(distance):
                position[0] -= 1
                coordinates.add(tuple(position))
        if direction == "D":
            for _ in range(distance):
                position[1] -= 1
                coordinates.add(tuple(position))
        if direction == "U":
            for _ in range(distance):
                position[1] += 1
                coordinates.add(tuple(position))
    return coordinates

with open("Input.txt") as f:
    Intersections = None
    for instructions in setup_instructions(f):
        coords = calculate_all_coords(instructions)
        if not Intersections:
            Intersections = coords
        else:
            Intersections = Intersections.intersection(coords)
    by_distance = sorted(Intersections, key=lambda x:abs(x[0]) + abs(x[1]))
    print(sum(by_distance[0]))
