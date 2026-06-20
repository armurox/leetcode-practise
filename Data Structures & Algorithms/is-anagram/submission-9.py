class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 2, with hash_map
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        for elem in count_s:
            if count_s[elem] != count_t.get(elem, 0):
                return False
        return True