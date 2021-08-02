def jobSequence(sam):
    sam.sort(key = lambda x : x[2])
    
    look = [0] * len(sam)
    count = 0
    
    print(sam)
    
    for i in range(len(sam) - 1 , -1 , -1):
        j = sam[i][1] - 1
        
        while j >= 0:
            if look[j] == 0:
                look[j] = sam[i][2]
                count += 1
                break
            
            j -= 1
            
    return sum(look) , count        
                



sam1 = [(1,2,100) , (2,1,19) , (3,2,27) , (4,1,25) , (5,1,15)] 
sam2 = [(1,4,20) , (2,1,10) , (3,1,40) , (4,1,30)]
print(jobSequence(sam1))
