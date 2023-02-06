class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # if len(g) < len(s):
        #     return len(g)
        # elif len(s)==0:
        #     return []
        # return 1
        g.sort()
        s.sort()
        init_1=0
        init_2=0
        
        while init_1< len(g) and init_2< len(s):
            if s[init_2]>=g[init_1]:
                
                init_1+=1
            init_2+=1
        return init_1
        
        