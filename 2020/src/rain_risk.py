from collections import deque
from utils import read_and_load_input

facing = deque('ESWN')
steps = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
p1, p2 = 0, 0
waypoint = 10+1j
data = read_and_load_input("DAY12")

for line in data:
    op, arg = line[0], int(line[1:].strip())
    val = arg // 90
    if op == 'L':
        facing.rotate(val)
        for _ in range(val):
            waypoint = complex(-waypoint.imag, waypoint.real)
    if op == 'R':
        facing.rotate(-val)
        for _ in range(val):
            waypoint = complex(waypoint.imag, -waypoint.real)
    if op == 'F':
        step = steps.get(facing[0])
        p1 += step * arg
        p2 += waypoint * arg
    if op in facing:
        step = steps.get(op)
        p1 += step * arg
        waypoint += step * arg

def rain_risky_1():
    print(f"Solution 1: {int(abs(p1.real) + abs(p1.imag))}")

def rain_risky_2():
    print(f"Solution 2: {int(abs(p2.real) + abs(p2.imag))}")

if __name__ == '__main__':
    rain_risky_1()
    rain_risky_2()
