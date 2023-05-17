class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=set()
        queue=[]
        n=0
        
        for i in range(len(isConnected)):
            if isConnected[i][i]==1 and i not in visited:
                visited.add(i)
                queue.append(i)
                
                while queue:
                    value=queue.pop(0)
                    for j in range(len(isConnected)):
                        if isConnected[value][j]==1 and j not in visited:
                            queue.append(j)
                            visited.add(j)
                n+=1
                        
        return n
    
#     0 1 2
# 0   1 1 0
# 1   1 1 0
# 2   0 0 1
