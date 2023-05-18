class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        comp = set()
        for edge in edges:
            comp.add(edge[1])
            
        result = []
        for edge in edges:
            
            if edge[0] not in comp:
                result.append(edge[0])
                
        return list(set(result))