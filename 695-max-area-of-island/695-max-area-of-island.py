class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        visited=set()
        direction=[(0,1),(1,0),(-1,0),(0,-1)]
        isValid = lambda row, col: 0 <= row < m and 0 <= col < n and grid[row][col] == 1
  
        def dfs(row,col):
            area=1
            visited.add((row,col))
            for i in direction:
                new_r,new_c= row + i[0],col+ i[1]
                
                if isValid(new_r,new_c) and (new_r, new_c) not in visited:
                    area+=dfs(new_r,new_c)
            return area
        
        max_value=0
        for i in range(m):
            for j in range(n):
                if isValid(i,j) and (i,j) not in visited:

                    max_value=max(max_value,dfs(i,j))

        return max_value

        
