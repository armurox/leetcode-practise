class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the two strings do not have the same length
        # they cannot be anagrams
        if (len_s := len(s)) != len(t):
            return False
        # otherwise, we will construct to dictionaries of the array
        # and the dictionaries must be equal in order for the two to be
        # anagrams
        count_s = {}
        count_t = {}
        for i in range(len_s):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        for key in count_s.keys():
            if count_s[key] != count_t.get(key, 0):
                return False
        return True
