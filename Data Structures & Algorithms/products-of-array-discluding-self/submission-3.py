class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # with division
        # total_product = math.prod(nums)
        # output = []
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         output.append(math.prod(nums[:i]) * math.prod(nums[i + 1:]))
        #     else:
        #         output.append(total_product // nums[i])
        # return output

        # optimal prefix - postfix solution
        num_size = len(nums)
        output = [1] * num_size
        prefix = 1
        for i in range(num_size):
            output[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(num_size - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output

