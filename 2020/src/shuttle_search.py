import os
from itertools import count

def grab_timetable(DAY):
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/{DAY}.txt', cur_path)
    with open(input_path, 'r') as file:
        raw_timetable = file.readlines()
        earliest_departure = int(raw_timetable[0].rstrip())
        bus_lines = raw_timetable[1].split(',')
        bus_lines_with_numbers = []
        for bus in bus_lines:
            try:
                bus_lines_with_numbers.append(int(bus))
            except:
                bus_lines_with_numbers.append(bus)
    return earliest_departure, bus_lines_with_numbers


def find_earliest_bus_id_timestamp(timetable):
    bus_id_timestamp = []
    for bus in timetable[1]:
        aligned_timestamp = timetable[0]
        if isinstance(bus, int):
            while aligned_timestamp % bus != 0:
                aligned_timestamp += 1
            bus_id_timestamp.append((bus, aligned_timestamp))
    bus_to_grab = bus_id_timestamp[0]
    for return_items in bus_id_timestamp:
        if return_items[1] < bus_to_grab[1]:
            bus_to_grab = return_items
    return bus_to_grab


def answer_calculation(original_time, bus_id_timestamp):
    wait_time = bus_id_timestamp[1] - original_time
    return bus_id_timestamp[0] * wait_time


def shuttle_search_1():
    the_timetable = grab_timetable('DAY13')
    earliest_bus_and_id = find_earliest_bus_id_timestamp(the_timetable)
    return answer_calculation(the_timetable[0], earliest_bus_and_id)


def sync(buses):
    indices = [i for i, bus in enumerate(buses) if bus]
    diff = indices[-1] - indices[0]
    prod = reduce(lambda a, b: a * b, filter(None, buses))
    return sum((diff - i) * pow(prod // n, n - 2, n) * prod // n
               for i, n in enumerate(buses) if n) % prod - diff

def shuttle_search_2():
    cur_path = os.path.dirname(__file__)
    input_path = os.path.relpath(f'../inputs/DAY13.txt', cur_path)
    with open(input_path) as f:
        timestamp, buses = [l.strip() for l in f]
        buses = sorted([(int(bus), idx) for idx, bus in enumerate(buses.split(',')) if bus != 'x'], reverse=True)

    timetable, step = 0, 1
    for bus, offs in buses:
        for c in count(t, step):
            if (c + offs) % bus == 0:
                timetable, step = c, step * bus
                break
    return timetable


if __name__ == "__main__":
    print(f"Solutution 1 {shuttle_search_1()}")
    print(f"Solutution 2 {shuttle_search_2()}")
