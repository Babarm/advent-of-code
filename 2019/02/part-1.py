#!/usr/bin/env python3
import time

infile = './input.txt'

def main():
    start_time = time.time()

    # read puzzle input
    with open(infile) as f:
        program = list(map(int, f.read().split(',')))

    # make adjustments as laid out in description
    program[1] = 12
    program[2] = 2

    opcode = program[0]
    position = 0
    while opcode != 99:
        if opcode == 1: # add
            a = program[program[position + 1]]
            b = program[program[position + 2]]
            c = a + b
            program[program[position + 3]] = c
            position += 4
        elif opcode == 2: # multiply
            a = program[program[position + 1]]
            b = program[program[position + 2]]
            c = a * b
            program[program[position + 3]] = c
            position += 4
        opcode = program[position]

    print(program[0])
    end_time = time.time()
    print('completed in {:.3f} sec'.format(end_time - start_time))

if __name__ == '__main__':
    main()
