class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for elem in nums:
            if elem in hash_set:
                return True
            hash_set.add(elem)
        return False