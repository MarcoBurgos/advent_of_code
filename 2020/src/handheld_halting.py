import os

def read_and_load_input():
    DAY = "day8"
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/{DAY}.txt', cur_path)
    input = []

    with open(input_path) as input_file:
        input = [line.rstrip() for line in input_file]

    return input

def solve(input):
    one_time = True
    index = 0
    solution = 0
    instructions_visited = dict()
    infinite = True

    while one_time or index == len(input):
        instruction, value = input[index].split(" ")[0], int(input[index].split(" ")[1])

        if instruction == "nop":
            if index not in instructions_visited:
                instructions_visited[index] = True
                index += 1
            else:
                print(f"repeted at nop with {index}")
                one_time = False
                index += 1
        elif instruction == "jmp":
            if index not in instructions_visited:
                instructions_visited[index] = True
                index += value
            else:
                print(f"repeted at jmp with {index}")
                one_time = False
                index += value
        elif instruction == "acc":
            if index not in instructions_visited:
                instructions_visited[index] = True
                solution += value
                index +=1
            else:
                print(f"repeted at acc with {index} {input[index]}")
                one_time = False
                index +=1
        elif index == len(input):
            infinite = False


    return solution, infinite

def handheld_halting_1():
    input = read_and_load_input()
    solution = solve(input)[0]

    return(solution)

def handheld_halting_2():
    input = read_and_load_input()

    keep_going = True
    for index, value in enumerate(input):
        if value.startswith("nop"):
            input[index] = value.replace("nop", "jmp")
        elif value.startswith("jmp"):
            input[index] = value.replace("jmp", "nop")
        while keep_going:
            solution = solve(input)
            keep_going = solution[1]
    return(solution[0])


if __name__ == '__main__':
    #print(handheld_halting_1())
    print(handheld_halting_2())
