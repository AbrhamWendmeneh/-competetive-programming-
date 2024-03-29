class Solution:
    def isValid(self, s: str) -> bool:
        valid = [('{', '}'), ('(', ')'), ('[', ']')]

        stack = []

        for item in s:

            if len(stack)>0 and (stack[-1], item) in valid:

                stack.pop()

            else:
                stack.append(item)

        return len(stack)==0