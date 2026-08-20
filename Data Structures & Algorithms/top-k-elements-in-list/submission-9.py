class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        top_k_arr = [[]] * size
        counts = {}

        # Loop through all elements of nums, creating the counts array
        for elem in nums:
            counts[elem] = 1 + counts.get(elem, 0)
        for elem in counts:
            top_k_arr[counts[elem] - 1] = top_k_arr[counts[elem] - 1] + [elem]
        ans = []
        upto_k = 0
        for i in range(size):
            for elem in top_k_arr[size - i - 1]:
                ans.append(elem)
                upto_k += 1
                if upto_k == k:
                    return ans
                
        