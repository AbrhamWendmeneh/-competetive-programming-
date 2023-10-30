from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={}
        degree=[0]*numCourses
        
        for i, j in prerequisites:
            if j in graph:
                graph[j].append(i)
            else:
                graph[j]=[i]
            degree[i]+=1
        
        queue=deque()
        course_order=[]
        
        for i in range(numCourses):
            
            if degree[i]==0:
                queue.append(i)
                course_order.append(i)
                
        visited=set()
        
        
        while queue:
            
            node= queue.popleft()
            visited.add(node)
            
            if node in graph:
                
                for neigh in graph[node]:
                    
                    degree[neigh]-=1
                    
                    if degree[neigh]==0:
                        course_order.append(neigh)
                        
                        queue.append(neigh)
                
        if len(visited)==numCourses:
            return course_order
        return []
            
        