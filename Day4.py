import copy
import sys

inputliststring = []

class class1:
    def __init__(self, x , y):
        self.x = x
        self.y = y

def function(input):
    return output

if __name__ == '__main__':
    input = open('inputfiles/AdventOfCode2022_Input_Day4.txt', 'r')
    inputliststring = input.read().split('\n')

    pairs = []
    step1 = []
    answer = 0

    for l in inputliststring:
        step1 = l.split(',')
        e1 = step1[0].split('-')
        e2 = step1[1].split('-')
        e1s = int(e1[0])
        e1e = int(e1[1])
        e2s = int(e2[0])
        e2e = int(e2[1])
        pairs.append([[e1s,e1e],[e2s,e2e]])

    #part 1
    # for p in pairs:
    #     if p[1][0] >= p[0][0] and p[1][1] <= p[0][1]:
    #         answer += 1
    #         # stops double counting when the ranges are identical
    #         continue
    #
    #     if p[0][0] >= p[1][0] and p[0][1] <= p[1][1]:
    #         answer += 1

    # part 2
    for p in pairs:
        if p[0][0] <= p[1][0] <= p[0][1] or p[1][0] <= p[0][0] <= p[1][1]:
            answer += 1

    print(answer)
