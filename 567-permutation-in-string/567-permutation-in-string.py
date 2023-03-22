class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        low=0
        high=len(s1)
        while low<(len(s2)-len(s1)+1):
            if sorted(s2[low:low+high])==sorted(s1):
                # print(high)  
                return True
            else:
                low+=1
                
                # print(high)
        return False