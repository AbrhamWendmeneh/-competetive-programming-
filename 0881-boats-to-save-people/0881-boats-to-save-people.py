class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # we have to sort the people
        # p=[1,2,2,3,4,5,6,7] l=8

        
        people.sort()
        
        left=0
        right=len(people)-1
        
        count=0
        
        while right >= left:    
            
            if people[left] <= (limit - people[right]):
                left+=1
            right-=1
            count+=1
        return count
            
                