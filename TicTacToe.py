# My Board
def display_board(board):
    
    print('  | |')
    print(' ' + board[7] +  '|' + board[8] + '|' + board[9])
    print('  | |')
    print('-------')
    print('  | |')
    print(' ' + board[4] +  '|' + board[5] + '|' + board[6])
    print('  | |')
    print('-------')
    print('  | |')
    print(' ' + board[1] +  '|' + board[2] + '|' + board[3])
    print('  | |')

def player_input():

    value = ''
    while not (value == 'X' or value == 'O'):
        value = input('Player 1: Would you like to be X or O?').upper()

    if value == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker
           