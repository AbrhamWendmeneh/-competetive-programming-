from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        queue=deque([n])
        visited=set()
        level= 0
        while queue:
            size= len(queue)
            for _ in range(size):
                node=queue.popleft()
                if node==0:
                    return level
                for i in range(1,int(n**(1/2))+1):
                    nextval= node - i**2
                    if nextval not in visited:
                        visited.add(nextval)
                        queue.append(nextval)
            level+=1
        return -1