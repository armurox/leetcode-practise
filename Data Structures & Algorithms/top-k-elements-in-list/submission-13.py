class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Loop through the array, constructing a "counts" array
        counts = [[]] * len(nums)
        counts_dict = {}
        for i in range(len(nums)):
            counts_dict[nums[i]] = counts_dict.get(nums[i], 0) + 1
        # Create counts array now
        for num in counts_dict:
            counts[counts_dict[num] - 1] = counts[counts_dict[num] - 1] + [num]
        counts.reverse()
        result = 0
        ans = []
        for elem in counts:
            for num in elem:
                result += 1
                ans.append(num)
                if result == k:
                    break
            if result == k:
                break
        return ans