class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        return bin(int(a,2) +int(b,2))[2:]
    
    #the reason which I use [2:] is to avoid the default value of 0b

                
        