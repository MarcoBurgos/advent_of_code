from time import perf_counter
from utils import read_and_load_input

def rambunctious_recitation_1():
    spoken = [8,13,1,0,18,9]
    total_rounds = 2020
    for i in range(total_rounds - len(spoken)):
     for j in range(len(spoken) - 1, 0, -1):
      if(spoken[j - 1] == spoken[-1]):
       spoken += [len(spoken) - j]
       break
     else:
       spoken.append(0)
    return(spoken[-1])

def rambunctious_recitation_2():
    spoken = [8,13,1,0,18,9]
    total_rounds = 30000000
    last_times_spoken_dict = dict(zip(spoken, range(1, len(spoken) + 1)))
    last_time_spoken = None
    for turn in range(len(spoken) + 1, num_iterations + 1):
        spoken_num = 0 if last_time_spoken is None else (turn - 1) - last_time_spoken
        last_time_spoken = last_times_spoken_dict[spoken_num] if spoken_num in last_times_spoken_dict else None
        last_times_spoken_dict[spoken_num] = turn
    return(spoken_num)

if __name__ == '__main__':
    start = perf_counter()
    print(f"solution 1 is {rambunctious_recitation_1()} took {perf_counter() - start} ")

    start = perf_counter()
    print(f"solution 2 is {rambunctious_recitation_2()} took {perf_counter() - start} ")
