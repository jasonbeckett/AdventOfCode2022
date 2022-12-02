import copy
import sys

inputliststring = []


#FOR PART 1
# def roundoutcome(p1,p2):
#     output = 0
#
#     #Rock         A     X       1
#     #Paper        B     Y       2
#     #Scissors     C     Z       3
#
#     if p2 == 'X':
#         output += 1
#         if p1 == 'A':
#             output += 3
#         if p1 == 'C':
#             output += 6
#
#     if p2 == 'Y':
#         output += 2
#         if p1 == 'B':
#             output += 3
#         if p1 == 'A':
#             output += 6
#
#     if p2 == 'Z':
#         output += 3
#         if p1 == 'C':
#             output += 3
#         if p1 == 'B':
#             output += 6
#
#
#     return output

#FOR PART 2

def roundoutcome(p1,p2):
    output = 0

    #Rock         A     X       1
    #Paper        B     Y       2
    #Scissors     C     Z       3

    # loss
    if p2 == 'X':
        if p1 == 'A':
            output += 3
        if p1 == 'B':
            output += 1
        if p1 == 'C':
            output += 2

    # draw
    if p2 == 'Y':
        if p1 == 'A':
            output += 1
            output += 3
        if p1 == 'B':
            output += 2
            output += 3
        if p1 == 'C':
            output += 3
            output += 3

    # win
    if p2 == 'Z':
        if p1 == 'A':
            output += 2
            output += 6
        if p1 == 'B':
            output += 3
            output += 6
        if p1 == 'C':
            output += 1
            output += 6


    return output



if __name__ == '__main__':
    input = open('inputfiles/AdventOfCode2022_Input_Day2.txt', 'r')
    inputliststring = input.read().split('\n')

    totalscore = 0

    for l in inputliststring:
        totalscore += roundoutcome(l[0],l[2])

    print(totalscore)




