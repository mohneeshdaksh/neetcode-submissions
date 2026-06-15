class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            rows_check = []
            for j in range(len(board[0])):
                if board[i][j] in rows_check:
                    return False
                elif board[i][j] != ".":
                    rows_check.append(board[i][j])
        for k in range(len(board[0])):
            cols_check = []
            for l in range(len(board)):
                if board[l][k] in cols_check:
                    return False
                elif board[l][k] != ".":
                    cols_check.append(board[l][k])
        box_check = [[] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                box_num = ((i//3) * 3) + (j//3)
                if board[i][j] in box_check[box_num]:
                    return False
                elif board[i][j] != ".":
                    box_check[box_num].append(board[i][j])
        return True