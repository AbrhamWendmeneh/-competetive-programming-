from collections import deque
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph={}
        prob= [0]*n
        prob[start_node] = 1
        
      
        for i, (source, target) in enumerate(edges):
            
            if source in graph:
                graph[source].append([target, succProb[i]])
            else:
                graph[source] = [[target, succProb[i]]]
                
            if target in graph:
                graph[target].append([source,succProb[i]])
            else:
                graph[target]=[[source,succProb[i]]]
                
        queue=deque()
        queue.append(start_node)
        
        while queue:
            
            node=queue.popleft()
            if node in graph:
                
                for neighbor, prb in graph[node]:
                    newresult=prob[node]*prb
                               
                    if newresult > prob[neighbor]:
                        
                        prob[neighbor]=newresult
                        queue.append(neighbor)
                        
        return prob[end_node]
                    
                    
                
            
        