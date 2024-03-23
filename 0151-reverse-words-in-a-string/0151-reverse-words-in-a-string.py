class Solution:
    def reverseWords(self, s: str) -> str:
        
        temp = s.split(' ')
        
        return ' '.join([i for i in temp[::-1] if i])
        