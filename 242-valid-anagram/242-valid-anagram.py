class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #flag= False
        #ctr=[]
        #if len(s)!=len(t):
         #   return False
        #else:
         #   for i in s and t:
          #      for j in range(len(t)):
           #         if i!=t[j]:
            #            flag=False
             #           ctr=[]
                        
              #      else:
               #         flag=True
                #        ctr.append(j)                   
            #return len(ctr)==len(t)
        # dict1= {}
        # dict2= {}
        # for i in s:
        #     if i in dict1:
        #         dict1[i] += 1
        #     else:
        #         dict1[i] = 1
        # for i in t:
        #     if i in dict2:
        #         dict2[i] += 1
        #     else:
        #         dict2[i] = 1
        # return dict1 == dict2
        a=[]
        b=[]
        for i in s:
            a.append(i)
        for j in t:
            b.append(j)
        a.sort()
        b.sort()
        return a==b
       
        