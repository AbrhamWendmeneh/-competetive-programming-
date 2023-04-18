class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # max_len=max(len(word1),len(word2))
        # res=''
        # for i in range(max_len):
        #     if len(word1)-1<i:
        #         continue
        #     res+=word1[i]
        #     if len(word2)-1<i:
        #         continue
        #     res+=word2[i]
        # return res
        right=0
        left=0
        res=''
        
        #this is for the condition the two strings are less than to the value of thier corrspondant string values
        while left< len(word1) and right<len(word2):
            
            res+=word1[left]+ word2[right]
            right+=1
            left+=1
            
        #this for if one of the string size is lessthan to compete the value with the other string value in which it gives index out of range result if we try to cosider the two     
        while left<len(word1):
            
            res+=word1[left]
            left+=1
        #the same type to the above one only the values are different but they have same case   
        
        while right<len(word2):
            
            res+=word2[right]
            right+=1
            
        return res