# #matrix for Tic Tac Toe board
# 3 modes of paly:
# 1 - player 1 and player 2
# 2 - 1 computer with random move + player 2
# 3 - 1 computer with good strtegy + player 2

# 1. GUI
#     1.1. Matrix board = symbols 7 x 17
#     each dot has digit corresponding to symbol
#     #board 7 lines - 17 rows

# Dict for images
# 0 - no
# 1 - *
# 2 - |
# 3 - -
# 4 - X
# 5 - O

# 00000000000000000
# 00000000000000000
# 00000000000000000
# 00000000000000000
# 00000000000000000
# 00000000000000000

# test board
# 11111111111111111
# 10000020002000001
# 10033323332333001

# *****************
# *   X |   |     *
# *  ---|---|---  *
# *     | O |     *
# *  ---|---|---  *
# *     |   | O   *
# *****************

#    2.1. functions to chenge didgits in matrix
#    2.2. function to draw baord according info in matrix (board)

# 2. Matrix to save O and X positions (game logic)
# game_board = [[0,0,0],
#               [0,0,0],
#               [0,0,0]]

# 3. function to input new O or X coordinats
# max turn = 9
# odd - X
# even - O
#    function to check if this new position is free and in the range of the board
#    function to convert O and X position to Matrix board (GUI)

# 4. function to check who wins 3 (O or X in line or in cross line)

# 5. Loop until win or quit - ask users to input new position, check, draw on Board, 
# check if sombody win or symbol q to for Exit

img_dict = {
        0: " ",
        1: "*",
        2: "|",
        3: "-",
        4: "X",
        5: "O"
        }


#GUI
def make_board(board_y = 7, board_x = 17):
    empty_board = []
    for i in range(board_y):
        empty_board.append([])
        for j in range(board_x):
            empty_board[i].append(0)
    return empty_board
            
def drow_board(list, i_dict):
    for i in range(y):
        for j in range(x):
            print(i_dict.get(list[i][j]), end="" if j < x-1 else "\n")
       
def matrix_prnt(list):
    for i in range(y):
        for j in range(x):
            print(list[i][j], end="" if j < x-1 else "\n")

#Game logic 
game_board = [[0,0,0],
              [0,0,0],
              [0,0,0]]

#Game operations
#New move
def new_move(game_board, matrix, move, mode): #mode auto - 1 player = PC, norm - 2 players 
    def col_convert_matrix(r):
        y = int(r)*4
        return y 
    def row_convert_matrix(c):
        x = int(c)*2-1
        return x 
    def computer(i):
        computer_move = [[(2,2),(1,1),(1,3),(3,3),(3,1)],
                [(1,2),(2,3),(3,2),(2,1),],
                [(1,1),(1,3),(3,3),(3,1)],
                [(1,1),(3,3)],
                [(1,2),(3,1)],
                [(1,2),(3,2),(2,1),(2,3)],
                [(2,1),(2,3),(1,2),(3,2)],
                [(1,1),(1,2),(2,1),(2,2),(3,1),(3,2)],
            ]
        player_move = [ [(2,2)],
                [(1,2),(2,3),(3,2),(2,1)],
                [(1,1),(1,3),(3,3),(3,1)],
                [(1,1),(1,2),(3,1),(3,2)],
                [(1,1),(2,1),(1,3),(2,3)],
                ]
        
        
        if i == 1: #first PC move
            row, col = player_move[0][0]
                
        elif i == 3: #second PC move. If PL1 chose not corner cell - we go to corner
            for player_item in player_move[1]:
                row_pl, col_pl = player_item
                if game_board[int(row_pl)-1][int(col_pl)-1] == 2:
                    for item in computer_move[0]:
                            row, col = item
                            if game_board[int(row)-1][int(col)-1] == 0:
                                break
                    break
            for player_item in player_move[2]:
                row_pl, col_pl = player_item
                if game_board[int(row_pl)-1][int(col_pl)-1] == 2:
                    for item in computer_move[1]:
                            row, col = item
                            if game_board[int(row)-1][int(col)-1] == 0:
                                break
                    break
        elif i == 5:
            
            for cp_prev_item in computer_move[2]: #1 if 1 in corner
                row_cp, col_cp = cp_prev_item
                if game_board[int(row_cp)-1][int(col_cp)-1] == 1:
                    print("1 в углу")
                    for play_item in player_move[2]:
                        row_pl, col_pl = play_item
                        if game_board[int(row_pl)-1][int(col_pl)-1] == 2:
                            print("2 в углу")
                            if (int(row_pl) + int(col_pl)) == 4:
                                print("2 во втором или 4")
                                for item in computer_move[3]:
                                    row, col = item
                                    if game_board[int(row)-1][int(col)-1] == 0:
                                        break
                            else:
                                print("1 в первом или третьем ")
                                for item in computer_move[4]:
                                    row, col = item
                                    if game_board[int(row)-1][int(col)-1] == 0:
                                        break
                    break
            
                                                      
            for cp_prev_item in computer_move[1]:
                row_cp, col_cp = cp_prev_item
                if game_board[int(row_cp)-1][int(col_cp)-1] == 1: #not in corner
                    print("1 в кресте")
                    print(cp_prev_item)
                    #check for double 2 = OO
                      
                    if cp_prev_item == (1,2) or cp_prev_item == (3,2):
                        print("This is pos")
                        for item in computer_move[5]:
                            print(item)
                            row, col = item
                            if game_board[int(row)-1][int(col)-1] == 0:
                                break
                    else:
                        for item in computer_move[6]:
                            row, col = item
                            if game_board[int(row)-1][int(col)-1] == 0:
                                break
                    break    
                
            for play_item in player_move[3]:
                row_pl, col_pl = play_item
                if game_board[int(row_pl)-1][int(col_pl)-1] == 2 and game_board[int(row_pl)-1][int(col_pl) + 1-1] == 2:
                    if play_item == (1,1):
                        row, col = (1,3)
                        if game_board[int(row)-1][int(col)-1] == 0:
                                break
                    if play_item == (1,2):
                        row, col = (1,1)
                        if game_board[int(row)-1][int(col)-1] == 0:
                                break
                    if play_item == (3,1):
                        row, col = (3,3)
                        if game_board[int(row)-1][int(col)-1] == 0:
                                break
                    if play_item == (3,2):
                        row, col = (3,1)
                        if game_board[int(row)-1][int(col)-1] == 0:
                                break
                #vert
            for play_item in player_move[4]:
                row_pl, col_pl = play_item
                if game_board[int(row_pl)-1][int(col_pl)-1] == 2 and game_board[int(row_pl) +1 -1][int(col_pl) -1] == 2:
                    if play_item == (1,1):
                        row, col = (3,1)
                        if game_board[int(row)-1][int(col)-1] == 0:
                                break
                    if play_item == (2,1):
                        row, col = (1,1)
                        if game_board[int(row)-1][int(col)-1] == 0:
                                break
                    if play_item == (1,3):
                        row, col = (3,3)
                        if game_board[int(row)-1][int(col)-1] == 0:
                                break
                    if play_item == (2,3):
                        row, col = (1,3)
                        if game_board[int(row)-1][int(col)-1] == 0:
                                break
                # while True:
                #     print(1)
                #     row = random.randint(1, 3)
                #     col = random.randint(1, 3)
                #     if game_board[int(row)-1][int(col)-1] == 0:
                #         break
                    # elif:
                        # elif:
                    # for item in computer_move[2]:
                    #         row, col = item
                    #         if game_board[int(row)-1][int(col)-1] == 0:
                    #             break
                    
        elif i == 7:
            while True:
                row = random.randint(1, 3)
                col = random.randint(1, 3)
                if game_board[int(row)-1][int(col)-1] == 0:
                    break
            for item in computer_move[4]:
                row_cp, col_cp = item
                if game_board[int(row_cp)-1][int(col_cp)-1] == 1 and game_board[int(1)-1][int(3)-1] == 1:
                    if item == (1,1):
                        row, col = (1,2)
                        if game_board[int(row)-1][int(col)-1] == 0:
                                break
                if game_board[int(row_cp)-1][int(col_cp)-1] == 1 and game_board[int(3)-1][int(1)-1] == 1:
                    if item == (1,1):
                        row, col = (2,1)
                        if game_board[int(row)-1][int(col)-1] == 0:
                                break            
                if game_board[int(row_cp)-1][int(col_cp)-1] == 1 and game_board[int(3)-1][int(1)-1] == 1:
                    if item == (3,3):
                        row, col = (3,2)
                        if game_board[int(row)-1][int(col)-1] == 0:
                                break             
                if game_board[int(row_cp)-1][int(col_cp)-1] == 1 and game_board[int(1)-1][int(3)-1] == 1:
                    if item == (3,3):
                        row, col = (1,3)
                        if game_board[int(row)-1][int(col)-1] == 0:
                                break         
            for cp_prev_item in computer_move[2]:
                row_cp, col_cp = cp_prev_item
                if game_board[int(row_cp)-1][int(col_cp)-1] == 1:
                    print("1 в углу")
                    for item in computer_move[2]:
                            row, col = item
                            if game_board[int(row)-1][int(col)-1] == 0:
                                break
                    break
        else:
                while True:
                    row = random.randint(1, 3)
                    col = random.randint(1, 3)
                    if game_board[int(row)-1][int(col)-1] == 0:
                        break    
        
        return row, col 
    
    import random
    
    user = 2  if move % 2 == 0 else 1
    symb = "X" if user == 1 else "O"
    board_size = ["1","2","3"]
    if mode == "norm" or ((mode == "auto" or mode == "super_auto") and user == 2):
        while True:
            print(f"Player {user} input parametrs {symb} (input q to quit):") 
            row = (input("Input row: "))
            col = (input("Input col: "))
            if row in board_size and col in board_size:
                    if game_board[int(row)-1][int(col)-1] == 0:
                        print("OK")
                        game_board[int(row)-1][int(col)-1] = user
                        matrix[row_convert_matrix(row)][col_convert_matrix(col)] = user + 3
                        break
                    else:
                        print("This cell is busy.Try again.")
            elif row == "q" or col == "q":
                    print("Quit!")
                    return 0
            else:
                    print("New move out of board. Try again.")
    else:
        print("Computer move:")
        while True:
            if mode == "auto":
                row = random.randint(1, 3)
                col = random.randint(1, 3)
            if mode == "super_auto": #best move logic list
                row,col = computer(move)   
            
                    
            if game_board[int(row)-1][int(col)-1] == 0:
                game_board[int(row)-1][int(col)-1] = user
                matrix[row_convert_matrix(row)][col_convert_matrix(col)] = user + 3
                print(f"col = {col}, row = {row}.")
                break
                       
            
    return 1

# Check Win
def win(list):
    for player in range(1,3):
        symb = player
        # res = False
        for y in range(len(game_board)):
            win_line_row = True
            win_line_col = True
            win_cross_left = True
            win_cross_right = True
            for x in range(len(game_board)):
                win_line_row = win_line_row & (game_board[y][x] == symb) 
                win_line_col = win_line_col & (game_board[x][y] == symb)
                win_cross_left = win_cross_left & (game_board[x][x] == symb) 
                win_cross_right = win_cross_right & (game_board[x][2-x] == symb)
            if  win_line_row == True or  win_line_col == True or win_cross_left == True or  win_cross_right == True: 
                return player
                # break
    return 0
  

#tests
y = 7
x = 17

matrix_board = make_board()
    
#tests
def color_board(list_in):
    
    def top_bottom(list, line):
        for j in range(len(list[0])): #17
            list[line][j] = 1
        return list
    
    def horz_line(list, line):
        for j in [ 3,4,5,7,8,9,11,12,13]:
            list[line][j] = 3
        return list  

    def horz_play(list, line):
        for j in [0,16]:
            list[line][j] = 1
        for j in [6,10]:
            list[line][j] = 2
        return list  

    top_bottom(list_in, 0)
    top_bottom(list_in, 6)
    for i in range(1,len(list_in)-1):
        horz_play(list_in, i)
    horz_line(list_in, 2)
    horz_line(list_in, 4)    
    

# main program
y = 7
x = 17
color_board(matrix_board)
drow_board(matrix_board, img_dict)
#def input mode
mode_type = {
    "1": "norm",
    "2": "auto",
    "3": "super_auto",
    "q": "quit"
        }
while True:
    mode = input("Input mode: 1 - 2 players, 2 - player and computer, 3 - player and super computer and q for Exit: ")
    if mode in mode_type:
        mode = mode_type[mode]
        if mode == "quit":
            res = 0
        else:
            res = 1
            print(f"You will play in mode {mode}!!!")
        break
    else:
        print("Wrong symbol. Try again.")

print(res)

for i in range(1,10):
    if res == 0:
        print("Exit!") 
        break
    res = new_move(game_board, matrix_board, i, mode)  
    drow_board(matrix_board, img_dict)
    
    player_win = win(game_board)  
    if player_win in [1,2]: 
        print(f"Player {player_win} Win")
        break
    # elif win(game_board, 2): 
    #     print("Player 2 Win")
    #     break
    if i == 9: print("Game over! No move left.")
    

