class Solution:
    def simplifyPath(self, path: str) -> str:
        '''stack='/'
        emp=[]
        for k in (path):
            emp.append(k)
        
        for i in range(1,len(path)):
            if emp[i]=='/':
                # if emp[0]=='/':
                #     stack+=emp[0]
                if emp[i]=='/' and emp[i-1]=='/':
                    stack+=emp[i]
                elif i==len(emp)-1 and emp[i]=='/':
                    break
            elif emp[i]=='.' or emp[i-1]=='.':
                continue
            else:
                stack+=emp[i]
                
        return stack'''
        
        '''result=[]
        val=''
        for i in path+'/':
            if i=='/':
                if val=='..':
                    if result:
                        result.pop()
                elif val!='' and val!='.':
                    result.append(val)
                
                val=''
            else:
                val+=i
        
        return '/'+'/'.join(result)'''
        
        
        result=[]
        value_stack=path.split('/')
        
        for char in value_stack:
            
            if char=='..':
                if result:
                    result.pop()
            elif not char or char=='.':
                continue
            else:
                result.append(char)
                
        return '/'+ '/'.join(result)