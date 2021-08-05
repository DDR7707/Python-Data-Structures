def maximumPartition(s):
    n = len(s)
    res = ""
    
    look = [-1] * 26
    
    for i in range(n-1 , -1 , -1):
        if look[ord(s[i]) - ord("a")] == -1:
            look[ord(s[i]) - ord("a")] = i
    
    mini = -1
    
    for i in range(n):
        last = look[ord(s[i]) - ord("a")]
        
        mini = max(mini , last)
        
        if i == mini :
            res += s[i]
            
            print(res , end = " ")
            
            mini = -1
            
            res = ""
            
        else:
            res += s[i]
    return       
            
s = "ababcbacadefegdehijhklij"
maximumPartition(s)
