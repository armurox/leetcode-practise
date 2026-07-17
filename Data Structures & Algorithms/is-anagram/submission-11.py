class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the two lengths are not equal, they can't be anagrams
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        # get the count of each letter in each word
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        # if they match, isAnagram, otherwise not
        for key in count_s.keys():
            if count_s[key] != count_t.get(key):
                return False
        return True
        