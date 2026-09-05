class Solution:
    def grid_check(self,row,column,board):
            start_row,end_row = row[0],row[1]
            start_column, end_column = column[0],column[1]
            numbers={}
            for i in range(start_row,end_row):
                for j in range(start_column,end_column):
                    if board[i][j] not in numbers and board[i][j] != ".":
                        numbers[board[i][j]] = 1
                    elif board[i][j] in numbers:
                        return False
            return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Dictionary of loops rows vs item. Search through all dictionaries for an item, and if it appears more than once cancel
        """
        rows = {
            i:{} for i in range(9)
        }
        columns = {
            j:{} for j in range(9)
        }
        for i in range(9):
            for j in range(9):

                value = board[i][j]
                if value == ".":
                    continue
                
                if value not in columns[j]:
                    columns[j][value]=1
                else: return False
                if value not in rows[i]:
                    rows[i][value]=1
                else: return False

        grids = []
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                grids.append([[r, r + 3], [c, c + 3]])

        for i in grids:
            row,column = i[0],i[1]
            if not self.grid_check(row,column,board):
                return False
        return True