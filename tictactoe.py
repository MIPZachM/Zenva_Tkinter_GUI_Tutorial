# DEFINE ROWS
row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]

# DEFINE GAME STATES
is_running = True
p2_turn = False
p1_won = False
p2_won = False

# DEF - PRINT_GAME_BOARD
def print_game_board():
    global row1, row2, row3
    print(" | ".join(row1))
    print(" | ".join(row2))
    print(" | ".join(row3))
    print("\n\n")
    check_win_condition()

# DEF - GET INPUT
def get_input():
    global row1, row2, row3, p2_turn

    if not p2_turn:
        user_input = input("Player 1, please enter a row and column as 'row (1-3),column (1-3)': ").replace("'","")
        row,column = int(user_input.split(",")[0]), int(user_input.split(",")[1])

        if row == 1:
            row1[column - 1] = 'X'
        elif row == 2:
            row2[column - 1] = 'X'
        elif row == 3:
            row3[column - 1] = 'X'
        else:
            print("Invalid input, please try again!")
    else:
        user_input = input("Player 2, please enter a row and column as 'row (1-3),column (1-3)': ").replace("'","")
        row,column = int(user_input.split(",")[0]), int(user_input.split(",")[1])

        if row == 1:
            row1[column - 1] = 'O'
        elif row == 2:
            row2[column - 1] = 'O'
        elif row == 3:
            row3[column - 1] = 'O'
        else:
            print("Invalid input, please try again!")
    
    p2_turn = not p2_turn

# DEF - CHECK WIN ROW
def check_win_row(game_table, row=0):
    global p1_won, p2_won
    row_string = "".join(game_table[row])
    if row_string == "XXX":
        p1_won = True
    elif row_string == "OOO":
        p2_won = True

# DEF - CHECK WIN COLUMN
def check_win_column(game_table, col=0):
    global p1_won, p2_won
    col_string = "".join([
        game_table[0][col],
        game_table[1][col],
        game_table[2][col]
    ])
    if col_string == "XXX":
        p1_won = True
    elif col_string == "OOO":
        p2_won = True

# DEF - CHECK WIN DIAGONAL
def check_win_diagonal(game_table):
    global p1_won, p2_won
    first_diagonal = "".join([
        game_table[0][0],
        game_table[1][1],
        game_table[2][2]
    ])
    second_diagonal = "".join([
        game_table[0][2],
        game_table[1][1],
        game_table[2][0]
    ])
    if first_diagonal == "XXX" or second_diagonal == "XXX":
        p1_won = True
    elif first_diagonal == "OOO" or second_diagonal == "OOO":
        p2_won = True

# DEF - CHECK WIN ROWS
def check_win_rows(game_table):
    check_win_row(game_table, 0)
    check_win_row(game_table, 1)
    check_win_row(game_table, 2)

# DEF - CHECK WIN COLUMNS
def check_win_cols(game_table):
    check_win_column(game_table, 0)
    check_win_column(game_table, 1)
    check_win_column(game_table, 2)

# DEF - CHECK WIN CONDITION
def check_win_condition():
    global is_running, row1, row2, row3, p1_won, p2_won

    multi_dim_game_table = [row1,row2,row3]
    check_win_rows(multi_dim_game_table)
    check_win_cols(multi_dim_game_table)
    check_win_diagonal(multi_dim_game_table)

    if p1_won:
        print("*** PLAYER 1 WON! ***")
        is_running = False
    elif p2_won:
        print("*** PLAYER 2 WON! ***")
        is_running = False


# START GAME LOOP
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
while(is_running):
    get_input()
    print_game_board()
