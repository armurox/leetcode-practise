class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        hash_set = set()
        curr_len = 0
        l = 0
        r = 0
        for elem in s:
            if elem in hash_set:
                print(elem, s[l], l, curr_len, elem)
                count = 0
                while (elem in hash_set):
                    hash_set.remove(s[l])
                    l += 1
                    if count > 0:
                        curr_len -= 1
                    count += 1
                hash_set.add(elem)
            else:
                curr_len += 1
                hash_set.add(elem)
            if curr_len > max_len:
                max_len = curr_len
            r += 1
        return max_len