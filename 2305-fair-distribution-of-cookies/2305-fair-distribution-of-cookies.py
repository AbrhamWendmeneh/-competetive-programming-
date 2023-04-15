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
                #adding value
                bag_val[i]+=cookies[start_val]
                
                #calling the recursive function
                helper_function(start_val+1)
                
                #removing value 
                bag_val[i]-=cookies[start_val]
                
                #cheking if the bag_val is empty or not 
                if bag_val[i]==0:
                    break
                    
        helper_function(0)
        return self.val_ans
                
            