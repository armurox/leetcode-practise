class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        possible_answers = {}
        # Create a hash map as you loop through of each number and its index
        # at each stage, check if the difference between the target and the number exists in the array
        for i in range(len(nums)):
            if (first_index := possible_answers.get(target - nums[i])) is not None:
                return [first_index, i]
            possible_answers[nums[i]] = i
