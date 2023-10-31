from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        This is done by using the concept of dfs 
        
        '''
        graph={}
        visited=set()
        in_degree=[0]*numCourses
        
        for val1 , val2 in prerequisites:
            if val2 in graph:
                graph[val2].append(val1)
            else:
                graph[val2]=[val1]
                
            in_degree[val1]+=1
        stack=[]
        for i in range(numCourses):
            if in_degree[i]==0:
                stack.append(i)
        
        
        while stack:
            
            node=stack.pop()
            visited.add(node)
            if node in graph:
            
                for res in graph[node]:
                    in_degree[res]-=1

                    if in_degree[res]==0:
                        stack.append(res)
        return len(visited)==numCourses
            
            
        
        