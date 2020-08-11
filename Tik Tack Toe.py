import random
board = [' '*10]

def dispboard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inp():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Koushik do you want to be "X or O"?: ').upper()
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_cheaker(board, mark):
    return(board[7] == mark and board[8] == mark and board[7] == mark or board[4] == mark and board[5] == mark and
           board[6] == mark or board[1] == mark and board[2] == mark and board[3] == mark or board[7] == mark and
           board[4] == mark and board[1] == mark or board[8] == mark and board[5] == mark and board[2] == mark or
           board[9] == mark and board[6] == mark and board[3] == mark or board[7] == mark and board[5] == mark and
           board[3] == mark or board[1] == mark and board[5] == mark and board[9] == mark)

def choose_first():
    if random.randint(0, 1) == 0:
        return('Abhi')
    else:
        return('Koushik')

def space_avlb(board, position):
    return (board[position] == ' ')

def board_full(board):
    for x in range(1, 10):
        if space_avlb(board, x):
            return (False)
        return (True)

def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_avlb(board,position):
        try:
            position = int(input('Enter your position(1-9): '))
        except ValueError:
            print('please enter in integers only! ')
        return(position)

def replay():
    return(input('Do you want to play again? Enter Yes or No').upper().startswith('Y'))

print('Welcome to Tik Tack Toe Board')
while True:
    board=[' ']*10
    Koushik_marker,Abhi_marker=inp()
    turn=choose_first()
    print(turn + 'will go first !')
    play_game=input('Are you ready to play? Enter yes or no')
    if play_game.lower()[0]=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='Koushik':
            dispboard(board)
            position=player_choice(board)
            place_marker(board,Koushik_marker,position)
            if win_cheaker(board,Koushik_marker):
                dispboard(board)
                print('Congragulations! Koushik, you have won the game')
                game_on=False
            else:
                if board_full(board):
                    dispboard(board)
                    print('Game is drawn!!')
                    break
                else:
                    turn='Abhi'
        else:
            dispboard(board)
            position=player_choice(board)
            place_marker(board,Abhi_marker,position)
            if win_cheaker(board,Abhi_marker)==True:
                dispboard(board)
                print('Congragulations! Abhi, you have won the game')
                game_on=False
            else:
                if board_full(board):
                    dispboard(board)
                    print('Game is drawn!!')
                    break
                else:
                    turn='Koushik'

    if not replay():
        break



