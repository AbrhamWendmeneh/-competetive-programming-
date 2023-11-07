class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        count=1

        # dist= [dist[j] - speed[j] for j in range(len(dist))]
        # if dist[i] >=0 or i==0:
        #     count+=1
        # print(dist)
        
        time_val=[(dist[i])/ speed[i] for i in range(len(dist))]
        time_val.sort()
        
        # print(time_val)
        for i in range(1,len(dist)):
            if time_val[i]<=i:
                return count
            count+=1
                          
        return count