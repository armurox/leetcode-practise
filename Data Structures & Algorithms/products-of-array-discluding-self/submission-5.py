class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix_array = [1] * size
        suffix_array = [1] * size
        # Create prefix array
        prefix_product = 1
        for i in range(size):
            prefix_array[i] = prefix_product
            prefix_product *= nums[i]
        suffix_product = 1
        for i in reversed(range(size)):
            suffix_array[i] = suffix_product
            suffix_product *= nums[i]
        for i in range(size):
            suffix_array[i] = suffix_array[i] * prefix_array[i]
        return suffix_array