class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxprice=0
        # for i in range(len(prices)):
        #     if i <= min(prices):
        #         for j in range(i+1,len(prices)-1):
        #             maxprice=max(prices[j]-prices[i],maxprice)
        # return maxprice
#         left=0
#         right=len(prices)-1
#         max_profit=0
#         while right<len(prices) and right > left:
#             if prices[right]-prices[left]<=0:
#                 left+=1
#             else:
#                 max_profit=max(max_profit,(prices[right]-prices[left]))
                
#             right-=1
#         return max_profit
        left=0
        right=1
        max_profit=0
        while right<len(prices) :
            if prices[right]-prices[left]<=0:
                left=right
            else:
                max_profit=max(max_profit,(prices[right]-prices[left]))
                
            right+=1
        return max_profit