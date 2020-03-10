#!/usr/bin/env python3

import time

infile = './input.txt'

def main():
    start_time = time.time()

    # read puzzle input
    with open(infile) as f:
        data = []
        for line in f:
            data.append(list(map(int, line.split())))

    end_time = time.time()
    print('completed in {:.3f} sec'.format(end_time - start_time))

if __name__ == '__main__':
    main()
