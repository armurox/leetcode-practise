class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 1, sorting
        return  sorted(s) == sorted(t)