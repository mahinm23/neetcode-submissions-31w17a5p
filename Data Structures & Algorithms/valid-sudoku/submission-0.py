class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                digit = board[r][c]

                if digit != ".":

                    box_i = (r//3) * 3 + (c//3)

                    if digit in rows[r] or digit in cols[c] or digit in box[box_i]:
                        return False

                    rows[r].add(digit)
                    cols[c].add(digit)
                    box[box_i].add(digit)

        return True