from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        #creating a dictionary with default value
        rows = defaultdict(int)

        #adding the rows to the dict and counting them 
        for row in grid:
            rows[tuple(row)] += 1
        
        n = len(grid)
        paired = 0

        #get the columns and check for the pair
        for row in range(n):
            column = tuple(grid[col][row] for col in range(n))

            #counting the pairs
            if column in rows:
                paired += rows[column]
        
        return paired
        
        
