class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        total_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    total_island += 1
                    self.dfs((i, j), grid, visited)

        return total_island
    
    def dfs(self, root, grid, visited):
        m, n = len(grid), len(grid[0])
        visited[root[0]][root[1]] = True
        
        queue = [root]
        while(len(queue) > 0):
            node = queue.pop(0)
            
            for x, y in [(node[0]-1, node[1]), (node[0]+1, node[1]), (node[0], node[1]-1), (node[0], node[1]+1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == "1" and not visited[x][y]:
                    queue.append((x, y))
                    visited[x][y] = True