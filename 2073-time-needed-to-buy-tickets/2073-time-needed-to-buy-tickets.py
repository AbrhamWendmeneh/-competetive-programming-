class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        val=0
        for i in range(len(tickets)):
            if i<=k:
                val+=min(tickets[i],tickets[k])
            else:
                val+=min(tickets[i],tickets[k]-1)
        return val