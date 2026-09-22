class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        hash_set = set()
        curr_len = 0
        l = 0
        for elem in s:
            curr_len += 1
            if elem in hash_set:
                while (elem in hash_set):
                    hash_set.remove(s[l])
                    l += 1
                    curr_len -= 1
                hash_set.add(elem)
            else:
                hash_set.add(elem)
            if curr_len > max_len:
                max_len = curr_len
        return max_len