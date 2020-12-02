import os


def report_repair_part1():
    DAY = "day1"
    YEAR = 2020
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/{DAY}.txt', cur_path)

    with open(input_path) as input_file:
        numbers = []
        for number in input_file:
            numbers.append(int(number))

    for index, value in enumerate(numbers):
        pointer = 0
        if value == numbers[pointer]:
            pass
        else:
            while pointer < len(numbers):
                if (value + numbers[pointer] == YEAR):
                    print(f"found it {value} + {numbers[pointer]}")
                    return (value, numbers[pointer])
                pointer += 1

def report_repair_part2():
    DAY = "day1"
    YEAR = 2020
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/{DAY}.txt', cur_path)

    with open(input_path) as input_file:
        numbers = []
        hundreds = []
        for number in input_file:
            if len(number) == 4:
                hundreds.append(int(number))
                numbers.append(int(number))
            else:
                numbers.append(int(number))

    for number in hundreds:
        for num in numbers:
            pointer = 0
            while pointer < len(numbers):
                if(number + num + numbers[pointer] == 2020):
                    print(f"found it {number} - {num} - {numbers[pointer]}")
                    return (number, num, numbers[pointer])
                pointer += 1


if __name__ == "__main__":
    # response = report_repair_part1()
    # print(response[0] * response[1])
    response =report_repair_part2()
    print(response[0] * response[1] * response[2])
