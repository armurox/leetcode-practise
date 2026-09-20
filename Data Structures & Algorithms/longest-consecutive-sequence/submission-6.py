class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for elem in nums:
            if elem - 1 not in num_set:
                curr_len = 1
                while (elem + curr_len) in num_set:
                    curr_len += 1
                longest = max(longest, curr_len)
        return longest