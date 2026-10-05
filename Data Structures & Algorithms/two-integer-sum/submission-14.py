class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(n) -> Looping through all elements
        Space complexity: O(n) -> Hash map could be whole array (minus one), since we're guaranteed to find a solution
        """
        # create a hash_map, where the key is target - the current number
        # and the value is the index
        # then we loop through the array, checking if the current number
        # is in the hash_map
        hash_map = {}
        for i in range(len(nums)):
            if (first_index := hash_map.get(nums[i])) is not None:
                return [first_index, i]
            hash_map[target - nums[i]] = i