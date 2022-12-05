import copy
import sys

inputliststring = []
stacks = []
stack = []
instructions = []

for r in range(9):
    stacks.append(stack[:])

if __name__ == '__main__':
    input = open('inputfiles/AdventOfCode2022_Input_Day5.txt', 'r')
    inputliststring = input.read().split('\n')

    # setup stacks
    for l in inputliststring:
        if l[1] == '1':
            break
        for i, c in enumerate(l[1:len(l):4]):
            if c != ' ':
                stacks[i].append(c)

    #setup instructions
    startprocess = 0
    for l in inputliststring:
        if startprocess == 1:
            step1 = l.split('from')            
            move = int(step1[0].split('move ')[1])
            fromstack = int(step1[1].split(' to ')[0])
            tostack = int(step1[1].split(' to ')[1])
            instructions.append([move, fromstack , tostack])
        if l == '':
            startprocess = 1
        else:
            continue
  
    movefromstack = []
    movetostack = []
    cratestomove = []

    for i in instructions:
        numbertomove = i [0]
        stackfromindex = i[1] - 1
        stacktoindex= i[2] - 1

        movefromstack = stacks[stackfromindex][:]
        cratestomove = movefromstack[0:numbertomove][:]

        #part1
        #cratestomove.reverse()

        newmovefromstack = movefromstack[numbertomove:][:]
        newmovetostack = cratestomove + stacks[stacktoindex][:]

        stacks[stackfromindex] = newmovefromstack[:]
        stacks[stacktoindex] = newmovetostack [:]

    answer = ''
    for s in stacks:
        answer += s[0]

    print(answer)
