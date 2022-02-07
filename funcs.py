from random import random
from re import S

def startBoard():
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    index_one = round(random()*15)
    index_two = round(random()*15)

    while index_two==index_one:
        index_two = round(random()*15)

    board[index_one] = 2
    board[index_two] = 2

    return board

def newNumber(board):

    index = round(random()*15);

    while board[index] != 0:
        index = round(random()*15);
    #print(index)

    board[index] = 2
    return board


def shiftArrayBack(array, start, ref): #shift given array one step back (no rollover)
    #print("start value is" + str(start))
    l = len(array)
    newArray = array
    #while newArray[start] == ref:
    newArray[start:l-1] = array[start + 1:l]
    newArray[l - 1] = ref
    return newArray

def shiftArrayForward(array, start, ref): #shift given array one step forwards
    
    l = len(array)
    newArray = array
    #while newArray[l-start-1] == ref:
    newArray[1:start+1] = array[0:start]
    newArray[0] = ref
    return newArray

def applyMask(array, num): #get a 1 or 0 mask for whichever values match the inputted number

    out = [0] * len(array)

    for i in range(len(array)):
        if array[i] == num:
            out[i] = 1
    return out

""" def printBoard(board):
    sep_str = "_|_"
    print(board[0], board[1], board[2], board[3], sep=sep_str)
    print(board[4], board[5], board[6], board[7], sep=sep_str)
    print(board[8], board[9], board[10], board[11], sep=sep_str)
    print(board[12], board[13], board[14], board[15], sep=sep_str)
    print("\n") """


def convertNum(num):
    if num < 10:
        if num == 0:
            s = "____"
        else: 
            s = "__"+str(num)+"_"
    elif num < 100:
        s = "_"+str(num)+"_"
    elif num < 1000:
        s = "_"+str(num)
    elif num < 10000:
        s = str(num)
    else:
        s = "xxxx"
        print("too many digits")


    return s

def printBoard(board):

    for row in range(4):
        s = ""
        s += "|_"
        for col in range(4):
            s += convertNum(board[row*4 + col]) + "_|_"

        #s += "_|"
        s = s[0:len(s)-1]
        print(s)
    print("\n")

def move(board, direction):

    newBoard = board

    for m in range(4): #go down board each row or column at a time
        #print("m is " + str(m))
        vec_start_index = m*4 #index for start, converting 4x4 grid to the 16x1 array

        vec = [0, 0, 0, 0]

        if (direction=="left") | (direction=="right"): #rows
            vec = board[vec_start_index:vec_start_index + 4]
        else:        
            k = 0
            for count in range(3-m, len(board), 4):
                vec[k] = board[count]
                k = k + 1                             #columns
            #vec = board[range(3-m, len(board), 4)]
        l = len(vec)
        #print("vector is" + str(vec))

        if any(vec):
            #----------------add adjacent identical numbers, no matter if they're separated by zeros or not----------------------------
            
            if (direction=="left") | (direction=="up"):

                h = 0
                
                while h < l-1:
                    num1 = vec[h]
                    p = h + 1
                    while p < l:
                        num2 = vec[p]
                        if num1==num2:
                            vec[h] = 2*num1
                            vec[p] = 0
                        p = p + 1
                    h = h + 1
                
            else:
                h = l-1
                
                while h > 0:
                    num1 = vec[h]
                    p = h - 1
                    while p >= 0:
                        num2 = vec[p]
                        if num1==num2:
                            vec[h] = 2*num1
                            vec[p] = 0
                        p = p - 1
                    h = h - 1
            #----------get rid of 0s----------

            ref = 0 #don't want 0s
            ind = 0

            if (direction=="left") | (direction=="up"):
            #if flag==0: #left and up
                while ind < l-1:
                    mask = applyMask(vec, ref)
                    #print("mask is" + str(mask))

                    if any(vec[ind:]) == False:
                        ind = l

                    elif mask[ind]:
                        #print("ind is " + str(ind))
                        #print("mask[ind] is " + str(mask[ind]))
                        vec = shiftArrayBack(vec, ind, ref)
                        #print("new vector is" + str(vec))
                    else:
                        ind = ind + 1
                
                #newBoard[vec_start_index:vec_start_index + 4] = vec
                #print("final new vec is " + str(vec))
            else:                                           #right and down
                while ind < l-1:
                    mask = applyMask(vec, ref)
                    #print("mask is" + str(mask))

                    reverse_ind = l-ind-1
                    #print(reverse_ind)

                    if any(vec[0:reverse_ind+1]) == False:
                        ind = l

                    elif mask[reverse_ind]:
                        #print("ind is " + str(ind))
                        #print("mask[ind] is " + str(mask[ind]))
                        vec = shiftArrayForward(vec, reverse_ind, ref)
                        #print("new vector is" + str(vec))
                    else:
                        ind = ind + 1
                
  
            if (direction=="left") | (direction=="right"):
                newBoard[vec_start_index:vec_start_index + 4] = vec
            else:
                k = 0
                for count in range(3-m, len(board), 4):
                    newBoard[count] = vec[k]
                    k = k + 1

    # print(board)
    # print(newBoard)
    return newBoard
            


