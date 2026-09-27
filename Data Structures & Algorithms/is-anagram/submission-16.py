class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the two strings are different lengths
        # then they cannot be anagrams of one another
        if (size := len(s)) != len(t):
            return False
        # loop through both, constructing a hash map of their counts
        # and see if equal
        s_counts = {}
        t_counts = {}
        for i in range(size):
            s_counts[s[i]] = 1 + s_counts.get(s[i], 0)
            t_counts[t[i]] = 1 + t_counts.get(t[i], 0)
        for elem in s_counts:
            if t_counts.get(elem, 0) != s_counts[elem]:
                return False
        return True