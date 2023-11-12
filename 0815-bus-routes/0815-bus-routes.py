from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source==target:
            return 0
        
        graph={}
        
        for val1, val2 in enumerate(routes):
            
            for i in val2:
                if i not in graph:
                    graph[i]=[]
                graph[i].append(val1)
         
            # for i in range(len(val2)):
            #     for j in range(1, len(val2)):
            #         if val2[i] not in graph:
            #             graph[val2[i]]=[]
            #         graph[val2[i]].append(val2[j])
            
        # print(graph)
        queue = deque()
        queue.append((source,0))
        visited=set()
        
        while queue:
            
            node, count=queue.popleft()
            
            if node == target:
                return count
            print(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    
                    visited.add(neigh)
                    
                    for next_stop in routes[neigh]:
                        queue.append((next_stop, count+1))

        return -1
