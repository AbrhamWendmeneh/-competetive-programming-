class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        

        dict_val={}
        
        for i in range(len(s)):
            
            if s[i] in dict_val.keys():
                
                dict_val[s[i]].append(i)
                
            else:
                
                dict_val[s[i]]=[i]
                
        #print(dict_val)
        
        collector=[]
        
        for j in dict_val:
            
            if len(dict_val[j])>1:
                
                collector.append(j)
                
        #print(collector)
        count=0
        
        for val in collector:
            
            first=dict_val[val][0]       # [0,1,4]
            second=dict_val[val][-1]
            
            count+=len(set(s[first+1:second]))
            
        return count

'''
The approach which I used in this case is

1) I use dictionary to store the value of all the chars which are found in the string 's' and this dictionary is used to store the value of the indexes which the repeated charaters are found and this is typically important for the opration what we do.

2) Based on this result which I get from the dictionary I store the chars which has frequency greater than 1 in which there is some property in the case of palindromes with some length.
For instance: a _ a for this example we have almost 26 characters can be filled to make the complete palindrome like this one a (a-z) a

3) And then based on the collected values from the collector array we can proceed to the next step which is try to iterate through the values in it and do some operations to get the first index and also the last index of the given char
in our case when s='aabca' collector only contains =['a'] and the value of 'a' in dict_val is {'a': [0,1,3]} 

first= 0
second= 3 based on the value which I get from I simple make set so as to ignore the repated value from the range which starts from first and ends at second 

4) Finally return the value of count 




'''                
        
        