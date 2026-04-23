
def isValidSudoku( board):
        hash1={}
        for i in range(9):
            hash1.clear()
            for j in range(9):
             if board[i][j].isnumeric():
               x=int(board[i][j])  
               hash1[x]=hash1.get(x,0)+1
               if hash1[x]>1:
                    return False        
        for j in range(9):
            hash1.clear()
            for i in range(9):  

             if board[i][j].isnumeric():
               y=int(board[i][j])
               hash1[y]=hash1.get(y,0)+1
               if hash1[y]>1:
                    return False
        for square in range(9):
            hash1.clear()
            for i in range(3):
                for j in range(3):
                    row=(square//3)*3+i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    y=int(board[row][col])
                    hash1[y]=hash1.get(y,0)+1
                    if hash1[y]>1:
                         return False

        return True
board=[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))
            