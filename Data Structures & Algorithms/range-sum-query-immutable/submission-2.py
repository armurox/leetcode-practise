class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        _sum = 0
        for elem in nums:
            _sum += elem
            self.prefix_sum.append(_sum)


    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]
        else:
            return self.prefix_sum[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)