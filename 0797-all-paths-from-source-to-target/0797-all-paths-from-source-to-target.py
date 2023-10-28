class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        adjList={}
        
        for i , neighbours in enumerate(graph):
            
            adjList[i]= neighbours

        stack=[(0,[0])]
        
        paths=[]
        
        while stack:
            
            node,path= stack.pop()
            
            if node ==len(adjList)-1:
                
                paths.append(path)
                  
            for neigh in adjList[node]:  
                
                stack.append((neigh,path+[neigh]))

        return paths
                
            
            
        