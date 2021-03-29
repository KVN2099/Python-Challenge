from random import randrange

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def is_draw():
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'O' and board[i][j] != 'X':
                return False
    return True

def draw_horizontal_line_values(values):
    if values:
        print('|', values[0], '|', values[1], '|', values[2], '|', sep='   ') # Vertical line with value
    else:
        print('|', '|', '|', '|', sep='       ') # Vertical line

def draw_horizontal_line_table():
    print('+', '+', '+', '+', sep='-------') # Horizontal line

def display_board(board):
    for i in range(3):
        draw_horizontal_line_table()
        draw_horizontal_line_values(0)
        draw_horizontal_line_values((board[i])) # Vertical line with value
        draw_horizontal_line_values(0)
    draw_horizontal_line_table()
    
def computer_move(legal_moves):
    if legal_moves:
        random_pair = legal_moves[randrange(len(legal_moves))]
        x = random_pair[0]
        y = random_pair[1]
        board[x][y] = 'O'
    else:
        board[randrange(3)][randrange(3)] = 'O'
    

def enter_move(num):
    pos = (num - 1) // 3, (num - 1) % 3
    if board[pos[0]][pos[1]] != 'X' and board[pos[0]][pos[1]] != 'O':
        board[pos[0]][pos[1]] = 'X'
        # Make array of available moves for computer
        legal_moves = []
        for i in range(3):
            for j in range(3):
                if isinstance(board[i][j], int):
                    legal_moves.append((i, j))
        computer_move(legal_moves)
    else:
        print('Please choose a legal move!')

def victory():
    for j in range(3):
        # Check rows
        if board[j][0] == board[j][1] == board[j][2]:
            return 'Computer' if board[j][0] == 'O' else 'Player 1'
        # Check columns
        if board[0][j] == board[1][j] == board[2][j]:
            return 'Computer' if board[0][j] == 'O' else 'Player 1'
        # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return 'Computer' if board[0][0] == 'O' else 'Player 1'
    if board[0][2] == board[1][1] == board[2][0]:
            return 'Computer' if board[1][1] == 'O' else 'Player 1'
    return False

print('Welcome to Tic Tac Toe!')
computer_move(0)
while True:
    winner = victory()
    if winner:
        display_board(board)
        print(winner, 'is the winner!')
        break
    elif is_draw():
        print('It is a draw!')
        break
    display_board(board)
    num = int(input('Please make a move: '))
    if num < 0 or num > 9:
        print('Illegal move!')
        break
    enter_move(num)