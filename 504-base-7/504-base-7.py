class Solution:
    def convertToBase7(self, num: int) -> str:
        base7 = ""
        isnegative = False        
        if num == 0:
            return "0"
        
        if num < 0:
            isnegative = True
            num = abs(num)

        while num > 0:
            remainder = num % 7
            base7 = str(remainder) + base7
            num //= 7
        if isnegative:
            base7 = "-" + base7

        return base7