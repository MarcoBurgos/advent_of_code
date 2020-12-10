import os

def read_and_load_input():
    DAY = "day9"
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/{DAY}.txt', cur_path)
    input = []

    with open(input_path) as input_file:
        input = [int(line.rstrip()) for line in input_file]

    return input

#Two Sum
def two_sum(num, array):
    left = 0
    right = len(array)-1
    while left < right:
        sum = array[right] + array[left]
        if sum == num:
            return True
        if sum > num:
            right -= 1
        else:
            left += 1
    return False


def encoding_error_1():
    input = read_and_load_input()
    preamble = 24
    for i in range(preamble,len(input)):
        solution = input[i+1]
        array = sorted(input[i-preamble:i+1])
        if not two_sum(solution,array):
            break
    return (solution)


def encoding_error_2(limit):
    input = read_and_load_input()
    left = 0
    right = len(input)-1
    for i in range(len(input)):
        for j in range(len(input) - 1):
            if sum(input[i:j]) == limit:
                if i == j-1 : continue
                return (min(input[i:j]) + max(input[i:j]))

if __name__ == '__main__':
    solution_1 = encoding_error_1()
    print(f"solution 1 is {solution_1}")
    print(f"solution 2 is {encoding_error_2(solution_1)}")
