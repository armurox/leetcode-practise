class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # with division
        total_product = math.prod(nums)
        output = []
        for i in range(len(nums)):
            if nums[i] == 0:
                output.append(math.prod(nums[:i]) * math.prod(nums[i + 1:]))
            else:
                output.append(total_product // nums[i])
        return output