import os
from utils import read_and_load_input

def text2chart(txt):
    D = {}
    for i, row in enumerate(txt):
        for  j, val in enumerate(row):
            D[complex(i, j)] = val
    return D

def changeseat(chart, seatkey):
    seat = chart[seatkey]
    if seat == '.':
        return seat
    occupied = 0
    for drxn in [-1, -1+1j, 1j, 1+1j, 1, 1-1j, -1j, -1-1j]:
        if chart.get(seatkey + drxn) == '#':
            occupied += 1
    if seat == 'L' and occupied == 0:
        return '#'
    if seat == '#' and occupied > 3:
        return 'L'
    return seat


def nextchart(chart):
    return {key: changeseat(chart, key) for key in chart.keys()}


def run_till_stabilized(chart):
    nc = nextchart(chart)
    while nc != chart:
        chart, nc = nc, nextchart(nc)
    return nc


def count_occupied(chart):
    return sum(v == '#' for v in chart.values())


def changeseat2(chart, seatkey):
    seat = chart[seatkey]
    if seat == '.':
        return seat
    occupied = 0
    for drxn in [-1, -1+1j, 1j, 1+1j, 1, 1-1j, -1j, -1-1j]:
        neighbor = '.'
        scale = 0
        while neighbor == '.':
            scale += 1
            neighbor = chart.get((scale * drxn) + seatkey)
        if neighbor == '#':
            occupied += 1
    if seat == 'L' and occupied == 0:
        return '#'
    if seat == '#' and occupied > 4:
        return 'L'
    return seat


def nextchart2(chart):
    return {key: changeseat2(chart, key) for key in chart.keys()}


def run_till_stabilized2(chart):
    nc = nextchart2(chart)
    while nc != chart:
        chart, nc = nc, nextchart2(nc)
    return nc


def seating_system_1():
    data = read_and_load_input("DAY11")
    empty_chart = text2chart(data)
    stabilized = run_till_stabilized(empty_chart)
    return count_occupied(stabilized)


def seating_system_2():
    data = read_and_load_input("DAY11")
    stabilized2 = run_till_stabilized2(text2chart(data))
    return count_occupied(stabilized2)

if __name__ == '__main__':
    print(seating_system_1())
    print(seating_system_2())
