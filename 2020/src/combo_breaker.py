from utils import read_and_load_input

def find_loop_size(subject, public_key, MOD):
    for i in range(MOD):
        if pow(subject, i, MOD) == public_key:
            return i

    return -1

def combo_breaker_1():
    input_data = read_and_load_input("Day25")
    card_public = int(input_data[0])
    door_public = int(input_data[1])
    MOD = 20201227
    card_loop_size = find_loop_size(7, card_public, MOD)
    return(pow(door_public, card_loop_size, MOD))

def combo_breaker_2():
    pass


if __name__ == '__main__':
    print(f"Solution 1: {combo_breaker_1()}")
    print(f"Solution 2: {combo_breaker_2()}")
