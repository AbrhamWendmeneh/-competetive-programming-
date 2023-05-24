class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        step=1
        q = deque()
        q.append((0,0))
        visited = set()
        visited.add((0,0))
        if grid[0][0] or grid[-1][-1]:
            return -1
        if row==1 and grid[0][0]==0:
            return 1
        
        
        directions =  [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        while q :
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    ndr, ndc = dr + r, dc + c

                    if 0<=ndr< row and 0 <= ndc <col and grid[ndr][ndc]==0 and (ndr,ndc) not in visited:

                        visited.add((ndr,ndc))
                        q.append((ndr,ndc))
                        if ndr ==row-1 and ndc ==col-1:
                            return step+1

            step += 1
        return  -1


