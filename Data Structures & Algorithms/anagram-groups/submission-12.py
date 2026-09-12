class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        # Loop through all strings
        for s in strs:
            # Put each string into a hash_map
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord('a')] += 1
            anagram_groups[tuple(counts)].append(s)
        return list(anagram_groups.values())
