def longestConsecutiveSequence(arr):
    look = set(arr)
    final = 0
    
    for i in range(len(arr)):
        if arr[i]-1 not in look:
            j = arr[i]
            
            while j in look:
                j += 1
            
            final = max(final , j-arr[i])
            
    return final        
    
    pass


arr = [2,6,1,9,4,5,3]
print(longestConsecutiveSequence(arr))
