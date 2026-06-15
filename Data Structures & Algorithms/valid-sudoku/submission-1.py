class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                box_num = (((i//3)*3) + (j//3))
                if v in rows[i] or v in cols[j] or v in boxes[box_num]:
                    return False
                rows[i].add(v)
                cols[j].add(v)
                boxes[box_num].add(v)
        return True
