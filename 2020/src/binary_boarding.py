import os

def find_missing(lst):
    return [x for x in range(lst[0], lst[-1])
                               if x not in lst]

def binary_boarding():
    DAY = "day5"
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/{DAY}.txt', cur_path)
    solution = 0
    data = []
    max_id = 0
    tickets = []

    with open(input_path) as input_file:
        data = [line.rstrip() for line in input_file]

    for b_pass in data:
        row_max = 127
        seat_max = 7
        seat_min = 0
        row_min = 0
        _row = b_pass[0:7]
        _col = b_pass[7::]
        for letter in _row:
            if letter == "F":
                row_max = ((row_max - row_min) // 2) + row_min

            else:
                row_min = ((row_max - row_min) // 2) + row_min + 1

        for letter in _col:
            if letter == "L":
                seat_max = ((seat_max - seat_min) // 2) + seat_min
            else:
                seat_min = ((seat_max - seat_min) // 2) + seat_min +1


        _id = row_min * 8 + seat_min
        tickets.append(_id)
        if _id > max_id:
            max_id = _id

    my_seat = find_missing(sorted(tickets))[0]
    return max_id, my_seat


if __name__ == '__main__':
    print(binary_boarding())
