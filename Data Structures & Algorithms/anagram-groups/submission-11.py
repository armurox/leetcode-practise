class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Set up the hashmap which will be construct
        grouped_anagrams = defaultdict(list)

        # For each string in the list
        # create the unique anagram hash_map
        # and update the grouped_anagrams hash_map
        # with the same
        for s in strs:
            count_s = [0] * 26
            for char in s:
                count_s[ord(char) - ord('a')] += 1
            grouped_anagrams[tuple(count_s)].append(s)
        return [value for value in grouped_anagrams.values()]
