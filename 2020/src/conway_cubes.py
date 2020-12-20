from collections import Counter
from itertools import product
from utils import read_and_load_input


def getNeighbors(cell):
    neighbors = [tuple(cell[i] + v[i] for i in range(len(cell))) for v in product([-1, 0, 1], repeat=len(cell)) ]
    neighbors.remove(cell)
    return neighbors

def playLife(layout, dimensions=2, cycles=6):
    assert(dimensions >= 2)
    living = [(x, y) + (0,)*(dimensions - 2) for x, line in enumerate(layout) for y, cell in filter(lambda c: c[1] == '#', enumerate(line))]
    for cycle in range(cycles):
        neighbors = Counter(neighbor for cell in living for neighbor in getNeighbors(cell))
        living = [cell for cell, neighborCount in filter(lambda x: x[1] == 3 or x[0] in living and x[1] == 2, neighbors.items())]
    return len(living)

def conway_cubes_1():
    input = read_and_load_input("DAY17")
    return playLife(input, 3)


def conway_cubes_2():
    input = read_and_load_input("DAY17")
    return playLife(input, 4)


if __name__ == '__main__':
    print(f"Solution 1: {conway_cubes_1()}")
    print(f"Solution 2: {conway_cubes_2()}")
