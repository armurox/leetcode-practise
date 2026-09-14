class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Attempt 1: Unrolling the matrix into a 1-D array, and doing 
        # binary search on it: O (m + log(m * n))

        # Step 1: unroll the matrix
        unrolled_matrix = []
        for row in matrix:
            unrolled_matrix += row
        # Step 2: Carry out standard binary search
        start = 0
        end = len(unrolled_matrix) - 1
        while start <= end:
            middle = (start + end) // 2
            # If middle is larger than target, search left half
            if unrolled_matrix[middle] > target:
                end = middle - 1
            elif unrolled_matrix[middle] < target:
                start = middle + 1
            elif unrolled_matrix[middle] == target:
                return True
        return False
