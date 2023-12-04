class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        max_val= -1
        for i in range(1, len(num)-1):
            if int(num[i])==int(num[i-1]) and int(num[i])==int(num[i+1]):
                max_val= max(max_val, int(num[i]))
        if max_val!=-1:
            return str(max_val)*3
        return ""        