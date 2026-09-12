class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Contruct a hash map where every element's count is recorded
        count_map = {}
        for elem in nums:
            count_map[elem] = 1 + count_map.get(elem, 0)
        # Now, convert it into a hash_map of counts as keys with the elements
        counts_to_elems = [[]] * len(nums)
        for elem in count_map:
            counts_to_elems[count_map[elem] - 1] = counts_to_elems[count_map[elem] - 1] + [elem]
        ans = []
        upto_k = 0
        size = len(nums)
        for i in range(size):
            for elem in counts_to_elems[size - i - 1]:
                ans.append(elem)
                upto_k += 1
            if upto_k == k:
                return ans
        return []
        
            
            