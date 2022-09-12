#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    idx = 0
    if my_list:
        for i in range(x):
            try:
                print(my_list[i], end='')
                idx += 1
            except IndexError:
                break
    print("\n", end='')
    return idx
