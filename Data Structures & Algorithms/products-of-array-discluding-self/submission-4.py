class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix_arr = [1] * size
        suffix_arr = [1] * size
        # Construct prefix array
        for i in range(1, size):
            prefix_arr[i] = nums[i - 1] * prefix_arr[i - 1]
        # construct suffix arr
        for i in reversed(range(size - 1)):
            suffix_arr[i] = nums[i + 1] * suffix_arr[i + 1]
        result = [0] * size
        for i in range(size):
            result[i] = prefix_arr[i] * suffix_arr[i]
        return result