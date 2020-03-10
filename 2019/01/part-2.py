#!/usr/bin/env python3
import time

infile = './input.txt'

def calc_fuel(mass):
    return max((mass // 3) - 2, 0)

def main():
    start_time = time.time()

    # read puzzle input
    with open(infile) as f:
        masses = list(map(int, f.read().splitlines()))

    fuel_required = 0
    for mass in masses:
        fuel = calc_fuel(mass)
        fuel_required += fuel
        while fuel != 0:
            fuel = calc_fuel(fuel)
            fuel_required += fuel
    print(fuel_required)

    end_time = time.time()
    print('completed in {:.3f} sec'.format(end_time - start_time))

if __name__ == '__main__':
    main()
