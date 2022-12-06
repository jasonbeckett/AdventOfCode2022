import copy
import sys

inputliststring = []

if __name__ == '__main__':
    input = open('inputfiles/AdventOfCode2022_Input_Day6.txt', 'r')

    inputliststring = input.read().split('\n')
    string = ''

    for l in inputliststring:
        string += l

    currentblock = ''
    subblock = []

    for i, char in enumerate(string):
        currentblock = string[i:i+14]
        repeaters = 0
        subblock = []
        for li, l in enumerate(currentblock):
            if li == 0:
                subblock.append(l)
            else:
                if l in subblock:
                    repeaters += 1
                subblock.append(l)

        if repeaters == 0:
            print(currentblock, i + 14)
            sys.exit()
