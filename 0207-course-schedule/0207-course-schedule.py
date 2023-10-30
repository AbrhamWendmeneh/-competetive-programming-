from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph={}
        degree=[0]*numCourses
        
        for i, j in prerequisites:
            if j in graph:
                graph[j].append(i)
            else:
                graph[j]=[i]
            degree[i]+=1
        
        queue=deque()
        
        #in this place we have to find the value which has no prior course request
        # to begin our queue
        
        for i in range(numCourses):
            
            if degree[i]==0:
                queue.append(i)
                
        visited=set()
        
        
        while queue:
            
            node= queue.popleft()
            visited.add(node)
            
            if node in graph:
                
                for neigh in graph[node]:
                    
                    degree[neigh]-=1
                    
                    if degree[neigh]==0:
                        
                        queue.append(neigh)
        
        # this is to check if there is cycle or not and 
        # if there is cycle the length of the set is not equal to 
        # numCourses that we have in the input
        
        return len(visited) == numCourses
        
        