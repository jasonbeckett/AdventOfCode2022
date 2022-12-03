import copy
import sys

inputliststring = []

def function(input):
    return output

def priorityvalue(char):

    if 97 <= ord(char) <= 123:
        return ord(char) - 96
    else:
        return ord(char) - 38

def splitstring(string):
    length = int(len(string))

    part1 = string[0:int(length/2)]
    part2 = string[(int(length/2)):]

    return ([part1,part2])

if __name__ == '__main__':
    input = open('inputfiles/AdventOfCode2022_Input_Day3.txt', 'r')
    inputliststring = input.read().split('\n')

    totalpriority = 0
    stopflag = 0
    for l in inputliststring:
        stopflag = 0
        parts = splitstring(l)
        for char1 in parts[0]:
            if stopflag == 1:
                break
            for char2 in parts[1]:
                if stopflag == 1:
                    break
                if char1 == char2:
                    print(char1,priorityvalue(char1))
                    totalpriority += priorityvalue(char1)
                    stopflag = 1

    print(totalpriority)

