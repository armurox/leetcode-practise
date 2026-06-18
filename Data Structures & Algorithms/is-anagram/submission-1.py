class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map_1 = dict()
        hash_map_2 = dict()

        def add_count_to_hash_map(e: str, hash_map) -> None:
            if e in hash_map:
                hash_map[e] += 1
            else:
                hash_map[e] = 1

        for elem in s:
            add_count_to_hash_map(elem, hash_map_1)
        for elem in t:
            add_count_to_hash_map(elem, hash_map_2)
        return hash_map_1 == hash_map_2