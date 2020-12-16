from time import perf_counter


def rambunctious_recitation(total_rounds):
    spoken = [8,13,1,0,18,9]
    last_times_spoken_dict = dict(zip(spoken, range(1, len(spoken) + 1)))
    last_time_spoken = None
    for turn in range(len(spoken) + 1, total_rounds + 1):
        spoken_num = 0 if last_time_spoken is None else (turn - 1) - last_time_spoken
        last_time_spoken = last_times_spoken_dict[spoken_num] if spoken_num in last_times_spoken_dict else None
        last_times_spoken_dict[spoken_num] = turn
    return(spoken_num)

if __name__ == '__main__':
    start = perf_counter()
    print(f"solution 1 is {rambunctious_recitation(2020)} took {perf_counter() - start} ")

    start = perf_counter()
    print(f"solution 2 is {rambunctious_recitation(30000000)} took {perf_counter() - start} ")
