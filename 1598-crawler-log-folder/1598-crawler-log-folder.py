class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        '''first i try to intialize empty list that is used store the elements of the stack and then it is used for to return the value of the lenght of this list first i try to use counter=0 but in this case if '../' occurs many times my couner value goes to negative and it does not do what it '''
#         counter=[]
        
#         for i in logs:
            
#             if '/' in i and './' not in i and '../' not in i:
                
#                 counter.append(i)
                
#             elif '../' in i:
                
#                 if len(counter)>0:
                    
#                     counter.pop()
        
#         return len(counter)

        '''but know I fix the problem that appears in the first code'''
        counter=0
        for  i in logs:
            if '/' in i and './' not in i and '../' not in i:
                counter+=1
            elif '../' in i and counter>0:
                counter-=1
        return counter