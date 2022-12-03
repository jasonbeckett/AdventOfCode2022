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

if __name__ == '__main__':
    input = open('inputfiles/AdventOfCode2022_Input_Day3.txt', 'r')
    inputliststring = input.read().split('\n')

    totalpriority = 0
    stopflag = 0
    rucksacks = []
    group = []

    for i, l in enumerate(inputliststring):
        group.append(l)

        if (i+1) % 3 == 0:
            stopflag = 0
            for char1 in group[0]:
                if stopflag == 1:
                    break
                for char2 in group[1]:
                    if stopflag == 1:
                        break
                    for char3 in group[2]:
                        if stopflag == 1:
                            break
                        if char1 == char2 == char3:
                            print(char1)
                            totalpriority += priorityvalue(char1)
                            stopflag = 1

            group = []








    print(totalpriority)

