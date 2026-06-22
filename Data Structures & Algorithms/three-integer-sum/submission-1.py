class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        num_size = len(nums)
        answer_set = set()
        # starting number
        for i in range(num_size):
            # two pointers from it going forward
            j = i + 1
            k = num_size - 1
            target = 0 - nums[i]
            while j < k:
                if (curr_sum := nums[j] + nums[k]) < target:
                    j += 1
                elif curr_sum > target:
                    k -= 1
                elif curr_sum == target:
                    answer = sorted([str(nums[i]), str(nums[j]), str(nums[k])])
                    answer_set.add(','.join(answer))
                    j += 1
            ans = []
            for elem in answer_set:
                temp_ans = []
                for num in elem.split(','):
                    temp_ans.append(int(num))
                ans.append(temp_ans)
        return ans

