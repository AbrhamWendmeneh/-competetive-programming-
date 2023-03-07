class Solution:
    def reverseWords(self, s: str) -> str:
        
        '''first splitting the string and then iterate through the array that is formed by splitting the given string then changing it to be reversed and adding empty string to it to match with the solution of in a given format'''
        
        emp=''
        
        temp=s.split()
        
        for i in temp:
            
            emp+=i[::-1]+' '
            
        return emp[:len(emp)-1]