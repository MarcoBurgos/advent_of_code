import os
from utils import read_and_load_input

input = read_and_load_input("DAY10")

def adapter_array_1(input):
    numbers = read_and_load_input("DAY10")
    numbers.append(0)
    numbers.sort()
    differences = [numbers[i + 1] - x for i, x in enumerate(numbers[:-1])]
    return differences.count(1) * (differences.count(3) + 1)

def adapter_array_2(input):
    input = read_and_load_input("DAY10")
    numbers = sorted(input)
    combination_count = {0: 1}
    for num in numbers:
        combination_count[num] = 0
        combination_count[num] += combination_count.get(num - 1, 0)
        combination_count[num] += combination_count.get(num - 2, 0)
        combination_count[num] += combination_count.get(num - 3, 0)

    return combination_count[numbers[-1]]

if __name__ == '__main__':
    print(adapter_array_1(input))
    print(adapter_array_2(input))
