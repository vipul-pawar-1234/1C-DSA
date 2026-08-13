def isSafe(board,row,colm,n):
    for i in range(row):
        if board[i][colm] == "Q":
            return False
        
    i = row
    j = colm

    while i>=0 and j>=0:
        if board[i][j] == "Q":
            return False
        i-=1
        j-=1
    
    i = row
    j = colm

    while i>=0 and j<n:
        if board[i][j] == "Q":
            return False
        
        i-=1
        j+=1

    return True

def solve(board,row,n):

    if row == n: 
       for i in board: 
        for j in i:
            print(j,end=" ")
        print()
       return
    
    for colm in range(n):
        if isSafe(board,row,colm,n):

            board[row][colm] = "Q"

            solve(board,row+1,n)

            board[row][colm] = "."

            
n=4
board = [
    [".", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."]
]

solve(board,0,n)