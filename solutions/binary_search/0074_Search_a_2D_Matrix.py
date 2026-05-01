#self written solution using binary search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search
        def search(row: List[int], target) -> bool:
            low = 0
            high = len(row) - 1
            while low <= high:
                mid = (low + high) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        #decide which row to search   
        r = len(matrix) #rows
        c = len(matrix[0]) #columns
        for i in range(r):
            #edge cases
            if c == 1:
                if target == matrix[i][0]:
                    return True
            if target > matrix[i][0] and target < matrix[i][c - 1]:
                return search(matrix[i], target)
            elif target == matrix[i][0] or target == matrix[i][c - 1]:
                return True
        
        return False

#Standard solution using binary search
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2

            #convert mid to row and column indices
            row = mid // cols
            col = mid % cols

            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False