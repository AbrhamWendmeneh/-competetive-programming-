class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1]*len(graph)
        
        for i in range(len(graph)):
            if color[i]==-1:
                color[i]=1
                stack=[i]
                
                while stack :
                    
                    val=stack.pop()
                    
                    for con in graph[val]:
                        if color[con]== -1:
                            color[con]=1-color[val]
                            stack.append(con)
                        if color[con]==color[val]:
                            return False
                        
        return True
                        
            