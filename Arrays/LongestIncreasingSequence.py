def longestincreasingSequence(arr):
    
    look = [1] * len(arr)
    
    for i in range(len(arr) - 2 , -1 , -1):
        
        for j in range(i+1 , len(arr)):
            
            if arr[j] > arr[i]:
                
                look[i] = max(look[i] , look[j]+1)
        
    return max(look)        


arr = [10,9,2,5,3,7,101,18]

print(longestincreasingSequence(arr))
