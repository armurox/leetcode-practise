import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search version of the solution
        start = 1
        end = max(piles)
        while (start <= end):
            middle = (start + end) // 2
            # Compute the speed
            num_hours_taken = 0
            for i in range(len(piles)):
                num_hours_taken += math.ceil(piles[i] / middle)
            if num_hours_taken > h:
                start = middle + 1
            if num_hours_taken <= h:
                end = middle - 1
        return middle if num_hours_taken <= h else middle + 1