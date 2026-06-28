class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2_size = len(s2)
        s1_size = len(s1)
        if s2_size < s1_size:
            return False

        s1_counts = {}
        for elem in s1:
            s1_counts[elem] = 1 + s1_counts.get(elem, 0)
        for i in range((s2_size - s1_size) + 1):
            s2_counts = {}
            for j in range(i, i + s1_size):
                s2_counts[s2[j]] = 1 + s2_counts.get(s2[j], 0)
            if s1_counts == s2_counts:
                return True
        return False