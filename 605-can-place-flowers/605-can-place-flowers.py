class Solution:
    # @cache
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
#         low=0
#         high=len(flowerbed)-1
#         counter=0
#         while low<=high:
#             mid=low+(high-low)//2
            
#             if flowerbed[mid+1]==0 and flowerbed[mid-1]==0:
#                 counter+=1
#             elif flowerbed[mid+1]!=0:
#                 low=mid+1
#             else:
#                 high=mid-1
                
#         if counter!=0:
#             return True
#         return False
        counter=0
        val=[0]+flowerbed+[0]
        for i in range(len(val)):
            if val[i:i+3]==[0,0,0]:
                val[i+1]=1
                counter+=1
                
            else:
                continue
        return counter>=n
            
            
                