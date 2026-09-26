class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Time complexity: (O(n))
        Space complexity: (O(n))
        """
        # Initialize a set of seen values
        seen = set()
        # Loop through every element, and if the element 
        # exists in the hash set, then the set has a duplicate
        for elem in nums:
            if elem in seen:
                return True
            seen.add(elem)
        return False
