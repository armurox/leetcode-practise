class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}
        for i in range(len(nums)):
            count_nums[nums[i]] = 1 + count_nums.get(nums[i], 0)
        non_dup_nums = sorted(list(set(nums)), key = lambda a: count_nums[a])
        return non_dup_nums[-k:]
