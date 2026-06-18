class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check if each row is valid
        allowed_digits = [str(elem) for elem in range(1, 10)]
        allowed_digits.append('.')
        for row in board:
            found_elems = set()
            for elem in row:
                if (elem in found_elems and elem != '.') or elem not in allowed_digits:
                    return False
                found_elems.add(elem)
        # check if each column is valid
        for j in range(len(board)):
            found_elem = set()
            for i in range(len(board)):
                if (board[i][j] in found_elem and board[i][j] != '.') or board[i][j] not in allowed_digits:
                    return False
                found_elem.add(board[i][j])
        # check if each of the nine 3 x 3 sub-boxes are valid:
        for x in range(0, 7, 3):
            for i in range(0, 7, 3):
                found_elem = set()
                for j in range(3):
                    for k in range(3):
                        if (board[i + j][x + k] in found_elem and board[i + j][x + k] != '.') or board[i + j][x + k] not in allowed_digits:
                            return False
                        found_elem.add(board[i + j][x + k])
        return True


