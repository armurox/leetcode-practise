class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the two strings are not the same length
        # Then they are not anagrams
        if (size := len(s)) != len(t):
            return False

        # Create a hash_map with the counts of each letter
        count_s = {}
        count_t = {}
        for i in range(size):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        # The two hash_maps are equal, then the two strings are anagrams
        # otherwise they are not
        for letter in count_s.keys():
            if count_s[letter] != count_t.get(letter, 0):
                return False
        return True