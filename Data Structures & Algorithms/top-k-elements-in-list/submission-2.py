class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count_nums = {}
        # for i in range(len(nums)):
        #     count_nums[nums[i]] = 1 + count_nums.get(nums[i], 0)
        # non_dup_nums = sorted(list(set(nums)), key = lambda a: count_nums[a])
        # return non_dup_nums[-k:]
        count = {}
        size_nums = len(nums)
        freq = [[] for i in range(size_nums + 1)]
        for i in range(size_nums):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        for n, c in count.items():
            freq[c].append(n)
        upto_k = 0
        result = []
        print(freq)
        for i in range(len(freq) - 1, 0, -1):
            for res in freq[i]:
                result.append(res)
                upto_k += 1
                if upto_k == k:
                    return result

        
