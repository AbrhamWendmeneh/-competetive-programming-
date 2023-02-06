class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        e=[]
        a=sorted(score)
        # f=a[::-1]
        # b=a[-1]
        # c=a[-2]
        # d=a[-3]
        
        for i in score:
            
            if (a[::-1].index(i) == 0):
                
                e.append("Gold Medal")
                
            elif (a[::-1].index(i)==1):
                
                e.append("Silver Medal")
                
            elif (a[::-1].index(i)==2):
                
                e.append("Bronze Medal")
                
            else:
                
                e.append(str(a[::-1].index(i)+1))
                
        return e