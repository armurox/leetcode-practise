class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        hash_map = {}
        for i in range(len(nums)):
            if (first_num := nums[i]) in hash_map:
                return [hash_map[first_num], i]
            hash_map[target - nums[i]] = i