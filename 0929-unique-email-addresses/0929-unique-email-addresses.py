class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        set_val = set()
        
        for email in emails:
            
            local_name, domain_name = email.split('@')
            
            local_name = local_name.replace('.','')
            
            plus_pos = local_name.find('+')
            
            if plus_pos != -1:
                
                local_name = local_name[:plus_pos]
                
            processed_email = local_name + '@' + domain_name
            
            set_val.add(processed_email)
            
                
        return len(set_val)
                