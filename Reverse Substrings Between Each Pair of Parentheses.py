class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        deque = []
        for char in s:
            if char != ')':
                stack.append(char)
            else:
                while stack:
                    popped = stack.pop()
                    if popped != '(':
                        deque.append(popped)
                    else:
                        break
                # get the letters popped back to the stack in order
                for letter in deque:
                    stack.append(letter)
                deque = []
        return ''.join(stack)
        
