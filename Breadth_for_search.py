import queue
import numpy as np
from os import system
#
# def foundend(maze,steps):
#     i = startpos[0]
#     j = startpos[1]
#     for step in steps:
#         if step == 'l':
#             j -= 1
#
#         elif step == 'r':
#             j += 1
#         elif step == 'd':
#             i += 1
#         elif step == 'u':
#             i -= 1
#
#     print(f" path : {steps}cordinates {i},{j} item: {maze[i][j]}")
#     if (steps == 'dldd'):
#         print(f"Check STEPSSS : {steps} , {[j]},{j}, {maze[i][j]}")
#     if (maze[i][j] == "x"):
#         print(f'found path: {steps}')
#         return True;
#     return False


def printmaze(maze):
    for i in maze:
        for j in i:
            print(j,end=" ")
        print('',)

def printpath(maze,path):
    i = startpos[0]
    j = startpos[1]
    pos = set()
    for step in path:
        if step == 'l':
            j -= 1

        elif step == 'r':
            j += 1
        elif step == 'd':
            i += 1
        elif step == 'u':
            i -= 1
        # print((i,j))
        pos.add((i,j))
    # system('cls')
    for i,row in enumerate(maze):
        for j,ele in enumerate(row):
            if((i,j) in pos and ele !='x'):
                print("*",end=" ")
            else:
                print(ele,end=' ')
        print()


def validstep(maze,steps):
    i = startpos[0]
    j = startpos[1]
    pos =set()
    for step in steps:
        if step =='l':
            j-=1

        elif step =='r':
            j+=1
        elif step =='d':
            i+=1
        elif step =='u':
            i-=1
        pos.add((i,j))

        if ((i < 0 or i > len(maze)-1) or (j < 0 or j > len(maze[0])-1)):
            return False

        if (maze[i][j] == "x"):
            global notfinished
            notfinished = False
            print(f'path found : {steps}')
            printpath(maze, steps)
            return True

        if (maze[i][j] == "#"):
            return False;

    # system('cls')
    # for i, row in enumerate(maze):
    #     for j, ele in enumerate(row):
    #         if ((i, j) in pos and ele != 'x'):
    #             print("*", end=" ")
    #         else:
    #             print(ele, end=' ')
    #     print()
    return True



maze =[]
# maze.append(['#','#','o','#',])
# maze.append(['#',' ',' ','#',])
# maze.append(['#',' ','#','#',])
# maze.append(['#','x','#','#',])
maze.append(['#','#','#','#','#','#','#','o','#','#',])
maze.append([' ',' ','#','#',' ',' ',' ',' ',' ',' ',])
maze.append([' ',' ',' ',' ',' ','#','#',' ',' ',' ',])
maze.append(['#','#',' ','#',' ',' ',' ',' ','#',' ',])
maze.append(['#','#',' ','#','#','#','#',' ','#',' ',])
maze.append(['#','#',' ','#',' ',' ',' ',' ','#',' ',])
maze.append(['#','#',' ','#',' ','#','#',' ','#',' ',])
maze.append(['#','#',' ',' ',' ','#','#',' ','#',' ',])
maze.append(['#','#',' ','#','#','#','#','#','#',' ',])
maze.append(['#','#',' ','#','#','#',' ',' ',' ',' ',])
maze.append(['#','#','x','#','#','#','#','#','#','#',])

path = queue.Queue()
path.put("")
temp = ""

a = np.asarray(maze)
startpos = (np.where(a == 'o'))
startpos = (startpos[0][0],startpos[1][0])

endpos = (np.where(a == 'x'))
endpos = (endpos[0][0],endpos[1][0])
del a
notfinished=True;

printmaze(maze)
if __name__ == "__main__":
    while notfinished:
        temp = path.get()
        for i in ['l','r','u','d']:

            if(temp != '' and ((temp[-1]== 'u'and i == 'd')or (temp[-1] == 'd'and i == 'u')
                or (temp[-1] == 'r'and i == 'l') or (temp[-1] == 'l'and i == 'r'))):
                continue

            nextstep = temp+i

            if validstep(maze,nextstep):
                if(not notfinished):
                    break
                path.put(nextstep)
                # print(f'new steps: {nextstep}')
