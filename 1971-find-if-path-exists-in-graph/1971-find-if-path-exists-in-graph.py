class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Initialize an empty adjacency list
        
        adjc = [[] for i in range(n)]
        
        
        # Populate adjacency list with edges
        
        for val1, val2 in edges:
            adjc[val1].append(val2)
            adjc[val2].append(val1)
            
            
        # Initialize a queue with the source vertex 
        #and a set with the visited vertices
        
        queue=[source]
        visited=set(queue)
        # Perform a BFS algorithm on the graph
        
        
        while queue:
            # Pop the vertex at the front of the queue
            current=queue.pop(0)
            
            
            # Check if the current vertex is the destination
            if current == destination:
                return True
            
            
            else:
                
                # Add unvisited neighbors to the queue and visited set
                for neighbor in adjc[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        
        # If there are no more vertices in the queue or the 
        #destination vertex is not found, return False
        
        return False
