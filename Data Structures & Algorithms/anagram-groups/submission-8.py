class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for string in strs:
            anagram_array = [0] * 26
            for c in string:
                anagram_array[ord(c) - ord('a')] += 1
            hash_map[tuple(anagram_array)].append(string)
        return list(hash_map.values())
        