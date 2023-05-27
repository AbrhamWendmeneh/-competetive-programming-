class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        if num%3!=0:
            return []
        
        else:
            
            val=(num-3)//3
            res=[val,val+1,val+2]
            return res
        
#this question is a little bit tricky and I use math knowledge to do it and if you're good in math it is best for you 

#time complexity is Big O(1)
#spave complexity also Big O(1)