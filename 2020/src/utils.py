import os

def read_and_load_input(DAY):
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/{DAY}.txt', cur_path)
    input = []

    with open(input_path) as input_file:
        input = [(line.rstrip()) for line in input_file]

    return input
