class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left = 0
        right = size - 1
        while (left <= right):
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] == target:
                return middle
        return -1