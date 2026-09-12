class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        size = len(temperatures)
        result = [0] * size
        # create a stack of tuples, first element will be the index
        # second will be the element itself
        stack = [(0, temperatures[0])]
        for i in range(1, size):
            try:
                count = 1
                while temperatures[i] > stack[-1][1]:
                    while result[i - count] != 0:
                        count += 1
                    result[i - count] = i - stack.pop()[0]
            except IndexError:
                pass
            stack.append((i, temperatures[i]))
        return result
            
            
