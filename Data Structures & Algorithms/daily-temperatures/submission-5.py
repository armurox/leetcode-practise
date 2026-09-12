class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        size = len(temperatures)
        result = [0] * size
        # create a stack of tuples, first element will be the index
        # second will be the element itself
        stack = [(0, temperatures[0])]
        for i in range(1, size):
            while stack and temperatures[i] > stack[-1][1]:
                index, value = stack.pop()
                result[index] = i - index
            stack.append((i, temperatures[i]))
        return result
            
