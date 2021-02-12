import time
#Print the Sudoko board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 ==0 and j != 0:
                print(" | ", end="") # end="" means stay on the same line

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def read_board():
    board = []
    for i in range(9):
        print("Enter the 9 space separated elements of row {}".format(i) + " (use 0 for empty elements)")
        row = [int(x) for x in input().strip().split()]
        board.append(row)
    return board


#Pick the first empty square :
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None



#Check if the current board is valid :
def valid_board(board, num, pos):
    #board: our Sudoku board
    #num : the element (digit) that we have just added
    #pos : its position(i,j)

    # Check if their is any element equal to num in the same row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check if their is any element equal to num in the same column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check if their is any element equal to num in the same box
    # Get the position of the box(box_x, box_y) according to the position of one of its elements
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Loop throw all the elements of the box and check that is no digit which occurs twice
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            # we multiply box_x and box_y by 3 to get the correct positions of the elements of the current box
            # for example if we are in the box(0,2), we get its first element (0,6) by multiplying by 3
            # then, we iterate over its 9 elements (by adding 1, 2 or 3) and we check if their is any equality between them and the one we've just added
            if board[i][j] == num and (i,j) != pos:
                return False
    return True


def solve_board(board):
    #Step 1: Search for the first empty square
    find = find_empty(board)

    if not find:
        #Step 5: We have found a solution (a full valid sudoku board)
        return True
    else:
        #get the position of the empty square
        row, col = find

    for i in range(1,10):
        # iterate over the digits
        # Steps 2 and 3: For each one, check if it is valid if we place it in the empty square
        if valid_board(board, i, (row, col)):
            # Place the first valid digit in the empty square
            board[row][col] = i
            # Step 4: "Valid digit" case
            # We recursively call the function solve_board(board) with the new valid digit added to the board
            if solve_board(board):
                return True
            #Step 4: "Not valid digit" case
            board[row][col] = 0

    return False






#################################### MAIN PROGRAM ####################################
# to initilize the unsolved board, you can :
# - either use the following read_board() function and initialize it throw the console
#board= read_board()
# - Or, modify the example of the following sudoku board and use it directly
board =  [[5,1,7,6,0,0,0,3,4],
         [2,8,9,0,0,4,0,0,0],
         [3,4,6,2,0,5,0,9,0],
         [6,0,2,0,0,0,0,1,0],
         [0,3,8,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]


print("______________UNSOLVED SUDOKU BOARD______________ ")
print_board(board)
start = time.time()
solve_board(board)
end = time.time()
print("________________FINAL BOARD________________ ")
print_board(board)

print( "Solved in {} seconds".format( end - start ))