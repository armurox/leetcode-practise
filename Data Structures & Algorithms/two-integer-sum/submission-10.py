class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possible_answers = {}
        for i in range(len(nums)):
            if (first_index := possible_answers.get(target - nums[i])) is not None:
                return [first_index, i]
            possible_answers[nums[i]] = i
