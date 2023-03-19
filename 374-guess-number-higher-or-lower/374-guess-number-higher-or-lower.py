# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left = 0  # Initialize left endpoint of the search range to 0
        
        right = n - 1  # Initialize right endpoint of the search range to n-1

        # Keep searching until left endpoint is greater than right endpoint
        
        while left <= right:
            
            mid = left + (right - left) // 2 
            
            # Calculate the midpoint of the search range using integer division

            
            # Call the guess function with the midpoint and check its return                    value
            
            if guess(mid) == 0:  
                
                # If the guess is correct, return the midpoint as the answer
                return mid
            
            elif guess(mid) == 1: 
                
                # If the guess is too low, update the left endpoint to be the                       midpoint plus one
                left = mid + 1
            else:  
                # If the guess is too high, update the right endpoint to be the                 midpoint minus one
                right = mid - 1

        return left 
    
        # If no correct guess was found, return the value of the left endpoint            (which should be the smallest possible value not guessed) as the answer


