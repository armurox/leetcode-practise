class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        # construct max_left array
        max_left = [0] * len(height)
        max_val = 0
        height_size = len(height)
        for i in range(height_size):
            max_left[i] = max_val
            if height[i] > max_val:
                max_val = height[i]
        # construct max_right array
        max_right = [0] * height_size
        max_val = 0
        for i in reversed(range(height_size)):
            max_right[i] = max_val
            if height[i] > max_val:
                max_val = height[i]
        # find the total max area trappable
        for i in range(height_size):
            # add on the max area trappable by the current position
            curr_position_area = min(max_left[i], max_right[i]) - height[i]
            area += curr_position_area if curr_position_area >= 0 else 0
        return area
