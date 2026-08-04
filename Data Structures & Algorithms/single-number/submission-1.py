class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        second_seen = set()
        for elem in nums:
            if elem in seen:
                second_seen.add(elem)
            seen.add(elem)
        for elem in nums:
            if elem not in second_seen:
                ans = elem
        return ans