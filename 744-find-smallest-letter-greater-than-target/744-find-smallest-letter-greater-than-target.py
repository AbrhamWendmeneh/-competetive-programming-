class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # I have solved this question using for loop before and
        # now I want to solve it using binary search method
        # in which it is one of the related problem solving method
        
        low=0
        high=len(letters)-1
        
        while low<=high:
            middle=low+(high-low)//2
            
            if letters[middle]>target:
                high=middle-1
            else:
                low=middle+1
                
        if low==len(letters):
            
            return letters[0]
        
        return letters[low]
        