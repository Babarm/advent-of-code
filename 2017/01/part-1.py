#!/usr/bin/env python3

import time

infile = './input.txt'

def main():
    start_time = time.time()

    # read puzzle input
    with open(infile) as f:
        captcha = list(map(int, list(f.read())))

    limit = len(captcha)
    result = sum(captcha[i] for i in range(limit) if captcha[i] == captcha[(i + 1) % limit])

    print(result)

    end_time = time.time()
    print('completed in {:.3f} sec'.format(end_time - start_time))

if __name__ == '__main__':
    main()
