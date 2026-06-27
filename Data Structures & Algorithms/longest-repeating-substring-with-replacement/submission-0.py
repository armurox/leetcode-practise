class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0

        l = 0
        max_frequency = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_frequency = max(max_frequency, count[s[r]])

            # number of replacements
            while (r - l + 1) - max_frequency > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result
