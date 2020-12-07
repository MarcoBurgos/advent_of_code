import os

def validate_data(data):
    if len(data) == 8:
        return 1
    elif len(data) == 7:
        optional = 0
        for attribute in data:
            key = attribute.split(":")[0]
            if key == "cid":
                optional = 1
        if optional == 0:
            return 1
    return 0


def passport_processing_1():
    DAY = "day4"
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/{DAY}.txt', cur_path)
    solution = 0


    with open(input_path) as input_file:
        data = []
        passports_data = []
        passport = dict()
        for line in input_file:
            line = line.rstrip()
            if (len(line) > 1):
                params = line.split(" ")
                data.extend(params)
            else:
                solution += validate_data(data)
                data.clear()
        solution += validate_data(data)

    return solution

def validate_data_2(data):
    if len(data) == 8:
        return 1
    elif len(data) == 7:
        optional = 0
        for attribute in data:
            key = attribute.split(":")[0]
            if key == "cid":
                optional = 1
        if optional == 0:
            return 1
    return 0

def passport_processing_2():
    DAY = "day4"
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/{DAY}.txt', cur_path)
    solution = 0


    with open(input_path) as input_file:
        data = []
        passports_data = []
        passport = dict()
        for line in input_file:
            line = line.rstrip()
            if (len(line) > 1):
                params = line.split(" ")
                data.extend(params)
            else:
                solution += validate_data(data)
                data.clear()
        solution += validate_data(data)

    return solution



if __name__ == '__main__':
    print(passport_processing_1())
