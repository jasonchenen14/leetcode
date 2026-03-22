class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        if n == 0:
            return [[0]]
        
        prev_grid = self.specialGrid(n - 1)
        size = len(prev_grid)
        offset = size * size
        
        grid = []
        
        for r in range(size):
            row = []
            for c in range(size):
                row.append(prev_grid[r][c] + 3 * offset)
            for c in range(size):
                row.append(prev_grid[r][c])
            grid.append(row)
            
        for r in range(size):
            row = []
            for c in range(size):
                row.append(prev_grid[r][c] + 2 * offset)
            for c in range(size):
                row.append(prev_grid[r][c] + offset)
            grid.append(row)
            
        return grid
