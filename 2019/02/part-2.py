#!/usr/bin/env python3
import time

infile = './input.txt'

def main():
    start_time = time.time()

    # read puzzle input
    with open(infile) as f:
        program = list(map(int, f.read().split(',')))

    original = program.copy()

    found = False
    for noun in range(0, 100):
        if found:
            noun -= 1
            break
        for verb in range(0, 100):
            if found:
                verb -= 1
                break
            program = original.copy()
            program[1] = noun
            program[2] = verb

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

            if program[0] == 19690720:
                found = True

    print(100 * noun + verb)
    end_time = time.time()
    print('completed in {:.3f} sec'.format(end_time - start_time))

if __name__ == '__main__':
    main()
