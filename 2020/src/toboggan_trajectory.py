import os

def toboggan_trajectory_2():
    DAY = "day3"
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/{DAY}.txt', cur_path)

    with open(input_path) as input_file:
        input = []
        for line in input_file:
            input.append(line.rstrip())

    square = 0
    total_of_trees = 0
    lenght = len(input[0])
    flag = True
    for row in input:
        if flag:
            if square >= lenght:
                square -= lenght
            if (row[square] == '#'):
                total_of_trees += 1
            square += 1
        flag = not flag
    return total_of_trees


if __name__ == "__main__":
    print(toboggan_trajectory_2())
    #77x218x65x82x43
