class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        val=[[] for _ in range(n+1)]
        
        for i,j in dislikes:
            val[i].append(j)
            val[j].append(i)
        color=[-1]*(n+1)
        for i in range(1,n+1):
            if color[i]==-1:
                curr=[i]
                color[i]=1
                while curr:
                    stack=curr.pop()
                    
                    for con in val[stack]:
                        
                        if color[con]==-1:
                            color[con]= 1-color[stack]
                            curr.append(con)
                            
                        if color[con] == color[stack]:
                            return False
        return True
                        
                    
                