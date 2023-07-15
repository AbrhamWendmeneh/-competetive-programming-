class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top_row = 0
        bottom_row = len(matrix) - 1
        left_col = 0
        right_col = len(matrix[0]) - 1
        result = []

        while top_row <= bottom_row and left_col <= right_col:
            # traverse top row
            for i in range(left_col, right_col + 1):
                result.append(matrix[top_row][i])
            top_row += 1

            # traverse right column
            for i in range(top_row, bottom_row + 1):
                result.append(matrix[i][right_col])
            right_col -= 1

            # traverse bottom row
            if top_row <= bottom_row:
                for i in range(right_col, left_col - 1, -1):
                    result.append(matrix[bottom_row][i])
                bottom_row -= 1

            # traverse left column
            if left_col <= right_col:
                for i in range(bottom_row, top_row - 1, -1):
                    result.append(matrix[i][left_col])
                left_col += 1

        return result
