import copy
import sys

inputliststring = []

if __name__ == '__main__':
    input = open('inputfiles/AdventOfCode2022_Input_Day1.txt', 'r')
    inputliststring = input.read().split('\n')

    currentsum = 0
    sumlist = []
    
    for l in inputliststring:
        if l == '':
            sumlist.append(currentsum)
            currentsum = 0
        else:
            currentsum += int(l)

    sumlist.sort(reverse=True)
    print(sum(sumlist[0:3]))
