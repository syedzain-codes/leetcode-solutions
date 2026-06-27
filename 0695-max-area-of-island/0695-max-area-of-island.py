class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited=set()
        maximum=0
        def dfs(r,c):
            if r>len(grid)-1 or c>len(grid[0])-1 or r<0 or c<0:
                return 0
            if grid[r][c]==0:
                return 0
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            
            
            up=dfs(r-1,c)
            down=dfs(r+1,c)
            left=dfs(r,c-1)
            right=dfs(r,c+1)
            return 1+up+down+left+right
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visited:
                    count=dfs(i,j)
                    maximum=max(count,maximum)
        return maximum


        