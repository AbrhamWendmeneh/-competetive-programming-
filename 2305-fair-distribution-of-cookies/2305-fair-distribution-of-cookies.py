class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bag_val=[0]*k
        self.val_ans=float('inf')
        def helper_function(start_val):
            
            if start_val >= len(cookies):
                
                self.val_ans=min(max(bag_val),self.val_ans)
            if max(bag_val)>= self.val_ans:
                return 
            for i in range(k):
                
                bag_val[i]+=cookies[start_val]
                helper_function(start_val+1)
                bag_val[i]-=cookies[start_val]
                if bag_val[i]==0:
                    break
        helper_function(0)
        return self.val_ans
                
            