class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # increasing pointer
        num_size = len(numbers)
        l = 0
        r = num_size - 1
        while (sum_nums := numbers[l] + numbers[r]) != target:
            if sum_nums > target:
                r -= 1
            elif sum_nums < target:
                l += 1
        return [l + 1, r + 1]

        
        
        


        