class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        capitalized_words = []
        for word in words:
            if len(word) <= 2:
                capitalized_words.append(word.lower())
            else:
                capitalized_words.append(word[0].upper() + word[1:].lower())
        return ' '.join(capitalized_words)

#         s=''
        
#         temp=title.split()
        
#         for i in temp:
            
#             if len(i)<3 and temp.index(i)==0:
#                 s+=i.lower()
                
                
#             elif len(i)>=3 and temp.index(i)==0:
#                 s+=i.capitalize()
                
                
#             elif len(i)<3 and temp.index(i)!=0:
#                 s+=' '+i.lower()
                
                
#             elif len(i)>=3 and temp.index(i)!=0:
#                 s+=' '+i.capitalize()
#         return s


#         s = ''
#         setval=set()
#         temp = title.split()
        
#         for i in temp:
            
#             if len(i) < 3 and i not in setval:
#                 s += i.lower()
#                 setval.add(i)
                
#             elif len(i) >= 3 and i not in setval:
#                 s += i.capitalize()
#                 setval.add(i)
                
#             elif len(i) < 3:
#                 if i in setval:
#                     s += ' ' + i.lower()
#                 else:
#                     s += ' ' + i.lower()
                
#             elif len(i) >= 3:
#                 if i in setval:
#                     s += ' ' + i.capitalize()
#                 else:
#                     s += ' ' + i.capitalize()
                
#         return s

 