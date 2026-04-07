class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) #是一個字典他的key未知 但value是set
        cols = defaultdict(set) #用set是因為search快 O(1)
        box = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                box_index = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in box[box_index]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                box[box_index].add(val)
        return True