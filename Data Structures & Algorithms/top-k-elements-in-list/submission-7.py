class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        counts = [[]] * (size + 1)
        frequencies = {}
        # Construct dictionary of elements of counts per element
        for elem in nums:
            frequencies[elem] = 1 + frequencies.get(elem, 0)
        print(frequencies)
        # Store in array of frequencies, indexed by frequency, with the element itself as the value
        for elem in frequencies:
            counts[frequencies[elem]] = counts[frequencies[elem]] + [elem]
        ans = []
        count_index = 0
        i = 0
        print('test', counts)
        ans = []
        upto_k = 0
        for i in range(size):
            for elem in counts[size - i]:
                ans.append(elem)
                upto_k += 1
            if upto_k == k:
                return ans



        
