import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create a tuple array of positions and number of jumps to target
        # sorted by position (in reverse)
        size = len(position)
        jp_array = [()] * size
        for i in range(size):
            jp_array[i] = (((target - position[i]) / speed[i]), position[i])
        # create a final array of the distinct fleets
        jp_array.sort(key=lambda a: a[1], reverse=True)
        dp_array = [jp_array[0]]
        for i in range(1, size):
            if jp_array[i][0] > dp_array[-1][0]:
                dp_array.append(jp_array[i])
        return len(dp_array)


        
        

        