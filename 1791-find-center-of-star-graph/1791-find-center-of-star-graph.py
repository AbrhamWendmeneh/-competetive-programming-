class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a=edges[0]
        for i in range(1,len(edges)):
            
            a=list(set(a).intersection(edges[i]))
        return a[0]