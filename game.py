import funcs

from msvcrt import kbhit, getch


board = funcs.startBoard()

funcs.printBoard(board)

full = 0

while 1:

    if kbhit():
        key = ord(getch()) 
        
        #Arrow key numbers:
        #Up = 72
        #Left = 75
        #Down = 80
        #Right = 77
        
        if key==32:                                         #press space to reset the board whenever
            board = funcs.startBoard()
            funcs.printBoard(board)
            full = 0
        
        elif (key==224) & (full == 0):                      #if board isn't full and an arrow key is pressed
            oldBoard = board[:]
            subkey = ord(getch())
                
            if subkey == 72: 
                board = funcs.move(board, "up")
            elif subkey == 80:
                board = funcs.move(board, "down")
            elif subkey == 75: 
                board = funcs.move(board, "left")
            elif subkey == 77:
                board = funcs.move(board, "right")


            if board != oldBoard:
                board = funcs.newNumber(board)
                funcs.printBoard(board)

        if all(board):                                      #if board is full
            full = 1
            print("Game over, press space to reset\n")
    

