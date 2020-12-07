import os
from functools import reduce

def custom_customs_1():
    DAY = "day6"
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/{DAY}.txt', cur_path)
    solution = 0
    data = set()

    with open(input_path) as input_file:
        for line in input_file:
            line = line.rstrip()
            if (len(line) > 0):
                for character in line:
                    data.add(character)
            else:
                solution += len(data)
                data.clear()
        solution += len(data)
    return solution


def custom_customs_2():
    DAY = "day6"
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/{DAY}.txt', cur_path)

    return sum(
    [
        len(reduce(lambda set_1, set_2: set_1.intersection(set_2), [set(word) for word in g if word])) for g in
        [group.split('\n') for group in open(input_path).read().split('\n\n')]
    ])



if __name__ == '__main__':
    print(custom_customs_1())
    print(custom_customs_2())
