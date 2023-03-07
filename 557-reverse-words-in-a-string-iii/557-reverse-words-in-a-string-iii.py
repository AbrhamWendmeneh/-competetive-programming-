class Solution:
    def reverseWords(self, s: str) -> str:
#         emp=''
#         if len(s)==1:
#             return s
#         right=1
#         left=0
#         while right<len(s) and left<right:
#             if s[right]!=' ':
#                 right+=1
                
#             else:
#                 if s[right]==' ' and s[right]!=len(s)-1:
#                     emp+=s[left:right][::-1]+' '
#                     left+=(right-left+1)
#                     right+=2
#                 elif s[right]==len(s)-1:
#                     emp+=s[left:right][::-1]
                
#         return emp
    # def reverse_words(s):
    # Convert the string to a list of characters
        def reverse_sublist(lst, i, j):
            
            # Reverse the sublist between the given indices
            
            while i < j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1

        chars = list(s)

        # Initialize two pointers
        i, j = 0, 0

        # Loop through the list of characters
        while j < len(chars):
            # If we encounter a space, reverse the characters between the pointers
            
            if chars[j] == ' ':
                reverse_sublist(chars, i, j-1)
                i = j + 1
                
            # Move the second pointer forward
            j += 1

        # Reverse the last word in the string
        reverse_sublist(chars, i, j-1)
        

        # Convert the list of characters back to a string and return it
        
        return ''.join(chars)
    

        
                