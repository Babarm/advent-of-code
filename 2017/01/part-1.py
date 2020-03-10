#!/usr/bin/env python3

'''
Day 1
Inverse Captcha
Part 1
'''

infile = './input.txt'

def main():

    # read puzzle input into a list of integers
    with open(infile) as f:
        captcha = list(map(int, list(f.read())))

    limit = len(captcha)
    result = sum(captcha[i] for i in range(limit) if captcha[i] == captcha[(i + 1) % limit])

    print(result)

if __name__ == '__main__':
    main()
