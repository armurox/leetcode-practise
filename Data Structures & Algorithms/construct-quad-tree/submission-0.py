"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def has_same_vals(self, grid: List[List[int]]) -> bool:
        first = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != first:
                    return False
        return True


    def construct(self, grid: List[List[int]]) -> 'Node':
        # Check if the current grid has the same values
        if self.has_same_vals(grid):
            return Node(bool(grid[0][0]), True, None, None, None, None)

        n = len(grid)
        # Recurse for each of the children in the subgrid
        top_left = self.construct([row[0:n//2] for row in grid[0:n//2]])
        top_right = self.construct([row[n//2:n] for row in grid[0:n//2]])
        bottom_left = self.construct([row[0:n//2] for row in grid[n//2:n]])
        bottom_right = self.construct([row[n//2:n] for row in grid[n//2:n]])
        return Node(False, False, top_left, top_right, bottom_left, bottom_right)