class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        # setup the two pointers
        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]
        # continue until the two pointers are at the same place
        while (l < r):
            if max_l <= max_r:
                l += 1
                area += max(max_l - height[l], 0)
                max_l = max(height[l], max_l)
            else:
                r -= 1
                area += max(max_r - height[r], 0)
                max_r = max(height[r], max_r)
        return area


