class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a= ''
#         def find(word1):
            
#             for i in word1:#range(len(word1)):
#                 a+=i
#         if a==word2:
#             return True
#         else:
#             return False
        for i in word1:
            a+=i
        b=''    
        for j in word2:
            b+=j
        return a==b