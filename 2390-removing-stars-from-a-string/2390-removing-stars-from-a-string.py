class Solution:
    def removeStars(self, s: str) -> str:
        result=[]
        for i in s:
            if i != '*':
                result.append(i)
            else:
                result.pop()
        return ''.join(result)
                
                