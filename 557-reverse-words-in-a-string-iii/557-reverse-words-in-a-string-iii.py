class Solution:
    def reverseWords(self, s: str) -> str:
        val=s.split()
        res=''
        for i in val:
            res+=i[::-1]+' '
        
        return res[:-1]
        
    

        
                