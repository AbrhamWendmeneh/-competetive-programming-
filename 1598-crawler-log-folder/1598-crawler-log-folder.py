class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        '''first i try to intialize empty list that is used store the elements of the stack and then it is used for to return the value of the lenght of this list first i try to use counter=0 but in this case if '../' occurs many times my couner value goes to negative and it does not do what it '''
        

        '''but know I fix the problem that appears in the first code'''
        stack=[]
        for i in logs:
            if '/' in i and '../' !=i and './' !=i:
                stack.append(i)
            elif '../'==i:
                if len(stack)>0:
                    stack.pop()
        return len(stack)
         
        
    