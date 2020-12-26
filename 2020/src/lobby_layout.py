import sys
from utils import read_and_load_input


VECTORS = {
    'w' : (-4,  0),
    'e' : ( 4,  0),
    'nw': (-2, -3),
    'ne': ( 2, -3),
    'sw': (-2,  3),
    'se': ( 2,  3),
}


def parse(line):
    result = []
    while line:
        stepLength = 1 if line[0] in ('e', 'w') else 2
        result.append(line[:stepLength])
        line = line[stepLength:]
    return result


def walk(path):
    x, y = 0, 0
    for step in path:
        dx, dy = VECTORS[step]
        x += dx
        y += dy
    return x, y


def lobby_layout_1():
    result = set()
    for path in tiles:
        tile = walk(path)
        if tile in result:
            result.remove(tile)
        else:
            result.add(tile)
    return result


def neighbors(tile):
    yield from ((tile[0] + dx, tile[1] + dy) for dx, dy in VECTORS.values())


def lobby_layout_2(blackTiles):
    for day in range(100):
        newTiles = set()

        affectedTiles = blackTiles.copy()
        for tile in blackTiles:
            affectedTiles.update(neighbors(tile))

        for tile in affectedTiles:
            numNeighbors = sum(n in blackTiles for n in neighbors(tile))
            if tile in blackTiles:
                if numNeighbors in (1, 2):
                    newTiles.add(tile)
            else:
                if numNeighbors == 2:
                    newTiles.add(tile)

        blackTiles = newTiles

    return len(blackTiles)


if __name__ == '__main__':
    input_data = read_and_load_input("Day24")
    tiles = [parse(line.rstrip()) for line in input_data]
    blackTiles = lobby_layout_1()
    print(f"Solution 1: {len(blackTiles)}")
    print(f"Solution 2: {lobby_layout_2(blackTiles)}")
