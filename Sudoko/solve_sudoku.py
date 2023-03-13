
def find_empty_row_col(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    
    return None

def if_valid(board, number, position):
    for i in range(9):
        if board[position[0]][i] == number and i != position[1]:
            return False
    for i in range(9):
        if board[i][position[1]] == number and i != position[0]:
            return False
    
    x = position[1] // 3
    y = position[0] //3
    for i in range(y*3, y*3 + 3):
        for j in range(x*3, x*3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    
    return True

def solve(board):
    find = find_empty_row_col(board)
    if not find:
        return True
    
    for i in range(1, 10):
        if if_valid(board, i, find):
            board[find[0]][find[1]] = i

            if solve(board):
                return True
            
            board[find[0]][find[1]] = 0

    return False 

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
