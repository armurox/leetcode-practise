class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Space Complexity: O(n) -> The "seen" set in worst case
        Time Complexity: O(n) -> Loops through all elements of array when no duplicate
        """

        # Create a hash_set of seen values
        seen = set()
        for elem in nums:
            if elem in seen:
                return True
            seen.add(elem)
        return False