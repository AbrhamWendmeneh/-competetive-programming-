class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        num = len(pref)-1
        
        while num >= 1:
            
            pref[num]= pref[num]^pref[num-1]
            
            num -= 1
            
        return pref