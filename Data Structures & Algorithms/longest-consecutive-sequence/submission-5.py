class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # trying with sorting first
        # nums = list(set(nums))
        # nums = sorted(nums)
        # print('test', nums)
        # if len(nums) in [0, 1]:
        #     return len(nums)
        # longest_sequence = 0
        # current_sequence = 1
        # for i in range(1, len(nums)):
        #     if nums[i] - nums[i - 1] != 1:
        #         current_sequence = 0
        #     current_sequence += 1
        #     if current_sequence > longest_sequence:
        #         longest_sequence = current_sequence
        # return longest_sequence
        num_set = set(nums)

        longest = 0
        for elem in nums:
            if (elem - 1) not in num_set:
                length = 1
                while (elem + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest

