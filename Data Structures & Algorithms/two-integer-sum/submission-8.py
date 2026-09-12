class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force method
        size = len(nums)
        for i in range(size):
            for j in range(i + 1, size):
                if nums[i] + nums[j] == target:
                    return [i, j]