class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        for i in s:
            if i != '#' :
                stack1.append(i)
            elif stack1:
                stack1.pop()
        stack2=[]
        for j in t:
            if j != '#':
                stack2.append(j)
            elif stack2:
                stack2.pop()
        return stack1 == stack2
                
            
        