import re
import math
from utils import read_and_load_input


def docking_data_1():
    solution = 0
    memory = dict()
    mask = None
    mask_value = None
    input_data = read_and_load_input("DAY14")

    for line in input_data:
        if line.startswith("mask"):
            mask = re.search(r"\s*=\s*([\S\s]+)", line).group(1)
        elif line.startswith("mem"):
            memory_address = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
            value = int(re.search(r"\s*=\s*([\S\s]+)", line).group(1))
            value_bin = f"{value:036b}"
            value_after_mask = []

            for index, bit in enumerate(mask):
                if bit == "X":
                    value_after_mask.append(value_bin[index])
                else:
                    value_after_mask.append(mask[index])

            value_after_mask = "".join(value_after_mask)
            value_after_mask = int(value_after_mask, 2)
            memory[memory_address] = value_after_mask

    for k, v in memory.items():
        solution += v
    return solution

if __name__ == '__main__':
    print(docking_data_1())
