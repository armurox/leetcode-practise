class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_height = 0
        while (i < j):
            if (height := (j - i) * min(heights[i], heights[j])) > max_height:
                max_height = height
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_height
