class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        a=0
        # for i  in range(len(startTime)):
        #     if queryTime in [startTime[i],endTime[i]+1]:
        #         a+=1
        # return 
        for i in range(len(startTime)):
            if startTime[i]<=queryTime<=endTime[i]:
                a+=1
        return a
            