# PSEUDOCODE
# CREATE A VARIABLE CALLED BOARD INITIALIZED AS DICTIONARY WITH 9 #                                                   KEYS      1-9
# CREATE A VARIABLE CALLED ACTIVE, SET IT TO TRUE (BOOLEAN)
# CREATE A VARIABLE CALLED CURRENT_PLAYER, SET IT TO 'X'
# CREATE A VARIABLE CALLED NEXT_PLAYER, SET IT TO 'O'
# WHILE ACTIVE IS TRUE
    # PRINT THE BOARD
    # CREATE A VARIABLE CALLED VALID_MOVE, SET IT TO FALSE
    # WHILE VALID_MOVE IS FALSE
        # ASK CURRENT PLAYER TO PICK A MOVE
        # IF MOVE IS VALID
        # UPDATE BOARD (SET KEY AT INPUT TO CURRENT_PLAYER)
        # SET VALID_MOVE TO TRUE
# IF PLAYER HAS WON -- PRINT MESSAGE, SET ACTIVE TO FALSE
# ELSE IF THE BOARD IS FULL -- PRINT MESSAGE, SET ACTIVE TO FALSE
# ELSE SWITCH CURRENT PLAYER AND NEXT PLAYER

board = {
    '1': ' ',
    '2': ' ',
    '3': ' ',
    '4': ' ',
    '5': ' ',
    '6': ' ',
    '7': ' ',
    '8': ' ',
    '9': ' '
}

def print_board(): 
    print(f"""
    {board['1']} | {board['2']} | {board['3']} 1 2 3
    --+---+--
    {board['4']} | {board['5']} | {board['6']} 4 5 6
    --+---+--
    {board['7']} | {board['8']} | {board['9']} 7 8 9
    """)

def is_winner(b, player):
    return ((b['1'] == b['2'] == b['3'] == player) or # across the top
            (b['4'] == b['5'] == b['6'] == player) or # across the middle
            (b['7'] == b['8'] == b['9'] == player) or # across the bottom
            (b['1'] == b['4'] == b['7'] == player) or # down the left
            (b['2'] == b['5'] == b['8'] == player) or # down the middle
            (b['3'] == b['6'] == b['9'] == player) or # down the right
            (b['3'] == b['5'] == b['7'] == player) or # diagonal
            (b['1'] == b['5'] == b['9'] == player))   # diagonal

active = True
current_player = 'X'
next_player = 'O'
SPACES = list('123456789')

while(active):
    print_board()
    print(f"Your  move {current_player}")
    valid_move = False
    while not valid_move:
        space = input("Please enter a space: 1-9\n")
        print(f"You chose space {space}")
    # check if the move is valid 
        if space in SPACES and board[space] == " ":
            valid_move = True
            board[space] = current_player
    # check for end game state
    if is_winner(board, current_player):
        print("Huzzah!! You win!")
        print_board()
        active = False
    elif not ' ' in board.values():
        print("Cats game!")
        active = False
    else:
        current_player, next_player = next_player, current_player