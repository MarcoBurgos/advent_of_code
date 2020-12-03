import os


def password_philosophy_1():
    DAY = "day2"
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/{DAY}.txt', cur_path)
    response = 0

    with open(input_path) as input_file:
        input = []
        for line in input_file:
            params = line.rstrip().split(" ")
            params[0] = params[0].split("-")
            input.append(params)

    for line in input:
        min = int(line[0][0])
        max = int(line[0][1])
        character = line[1][0]
        password = line[2]
        occurrences = password.count(character)
        if min <= occurrences <= max:
            response += 1

    return response

def password_philosophy_2():
    DAY = "day2"
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/{DAY}.txt', cur_path)
    response = 0

    with open(input_path) as input_file:
        input = []
        for line in input_file:
            params = line.rstrip().split(" ")
            params[0] = params[0].split("-")
            input.append(params)

    for line in input:
        first_index = int(line[0][0])
        second_index = int(line[0][1])
        character = line[1][0]
        password = line[2]
        matches = 0

        if(password[first_index-1] == character):
            matches += 1

        if(password[second_index-1] == character):
            matches+= 1

        if matches == 1:
            response += 1

    return response


if __name__ == "__main__":
    #print(password_philosophy_1())
    print(password_philosophy_2())
