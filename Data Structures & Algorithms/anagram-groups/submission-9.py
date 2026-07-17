class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_arr_count = defaultdict(list)
        for elem in strs:
            count = [0] * 26
            for char in elem:
                count[ord(char) - ord('a')] += 1
            final_arr_count[tuple(count)].append(elem)
        return list(final_arr_count.values())