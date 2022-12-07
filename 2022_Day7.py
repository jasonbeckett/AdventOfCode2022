import copy
import sys

inputliststring = []
directoriesbylevel = []
totalusedspace = 0

class directory:
    def __init__(self, name,level):
        self.name = name
        self.level = level
        self.subdirectories = []
        self.files = []
        self.parentdirectory = self
        self.filesizetotal = 0

    def returnparent(self):
        return self.parentdirectory[0]

    def returnsubdirectory(self,subdirectoryname):
        for d in self.subdirectories:
            if d.name == subdirectoryname:
                return d
        return 'directory not found'

    def addsubdirectory(self,subdirectory):
        self.subdirectories.append(subdirectory)
        self.subdirectories[-1].parentdirectory = self

    def addfile(self,file):
        self.files.append(file)

class file:
    def __init__(self, name , size, parent):
        self.name = name
        self.size = size
        self.parentdirectory = parent

def showstructure(directory):
    print('******', directory.name, directory.level, directory.filesizetotal)

    for f in directory.files:
        print(f.name)

    for sb in directory.subdirectories:
        showstructure(sb)

    return 'Complete'

if __name__ == '__main__':
    input = open('inputfiles/AdventOfCode2022_Input_Day7.txt', 'r')
    inputliststring = input.read().split('\n')

    instruction = []

    topdirectory = directory('/',0)
    currentdirectory = topdirectory
    deepestlevel = 0

    level = []
    level.append(topdirectory)
    directoriesbylevel.append(level)
    level = []

    for l in inputliststring[1:]:
        instruction = l.split(' ')
        if instruction[0] == '$' and instruction[1] == 'cd':
            if instruction[2] == '/':
                currentdirectory = topdirectory
            else:
                if instruction[2] == '..':
                    currentdirectory = currentdirectory.parentdirectory
                else:
                    currentdirectory = currentdirectory.returnsubdirectory(instruction[2])

        if instruction[0] == '$' and instruction[1] == 'ls':
            continue

        if instruction[0].isnumeric() == True:
            size = int (instruction[0])
            totalusedspace += size
            currentdirectory.addfile(file(instruction[1],size,currentdirectory))

        if instruction[0] == 'dir':
            currentdirectory.addsubdirectory(directory(instruction[1], currentdirectory.level + 1))

            if currentdirectory.level + 1 > deepestlevel:
                deepestlevel += 1

            if (len(directoriesbylevel) - 1) < currentdirectory.level + 1:
                # add sub directory to new level
                directoriesbylevel.append([currentdirectory.subdirectories[-1]])
            else:
                # add sub directory to existing level
                directoriesbylevel[currentdirectory.level + 1].append(currentdirectory.subdirectories[-1])

    answer = 0

    # calculate directory sizes working up from deepest level direcotries and passing values up to parents
    stopflag = 0

    directorysizes = []

    for l in range(deepestlevel, -1, -1):
        for sb in directoriesbylevel[l]:
            print(sb.level,sb.name,sb.parentdirectory.name)
            for f in sb.files:
                sb.filesizetotal += f.size

            # part 1
            # if  sb.filesizetotal <+ 100000:
            #     answer += sb.filesizetotal

            # part 2
            directorysizes.append(sb.filesizetotal)
            sb.parentdirectory.filesizetotal += sb.filesizetotal

    spacerequired = 30000000 - (70000000 - totalusedspace)

    answer = 100000000000000000000000000
    for a in directorysizes:
        if  spacerequired <= a < answer:
            answer = a
    print(answer)



