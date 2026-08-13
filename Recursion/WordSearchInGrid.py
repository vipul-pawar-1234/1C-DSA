def search(board,word,i,j,index):
    if index == len(word):
          return True
    
    if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
          return False
    
    if board[i][j] != word[index]:
          return False
    
    temp = board[i][j]
    board[i][j] = "#"

    found = (
          search(board,word,i+1,j,index+1) or #D
          search(board,word,i-1,j,index+1) or #U
          search(board,word,i,j-1,index+1) or #L
          search(board,word,i,j+1,index+1)    #R
    )

    board[i][j] = temp

    return found

def exist(board,word):
        row = len(board)
        colm = len(board[0])

        for i in range(row):
              for j in range(colm):
                    
                    if search(board,word,i,j,0):
                          return True
        return False

board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "ABCCED"

print(exist(board,word))
