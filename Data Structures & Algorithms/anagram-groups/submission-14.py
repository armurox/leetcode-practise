class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time complexity: O(n * m) where n is number of strings, and m is number of letters
        Space complexity: O(n)
        """
        # Create dictionary of anagrams
        grouped_anagrams = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            grouped_anagrams[tuple(counts)].append(s)
        return list(grouped_anagrams.values())