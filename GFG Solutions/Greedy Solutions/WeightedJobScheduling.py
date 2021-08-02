def weightScheduling(sam):
    sam.sort(key = lambda x : x[1])
    
    look = [i[2] for i in sam]
    
    for i in range(1,len(sam)):
        j = 0
        while j < i:
            if sam[j][1] <= sam[i][0]:
                look[i] = max(look[i] , sam[j][2] + sam[i][2])
            j += 1
            
    return max(look)            



sam = [(1,2,50) , (3,5,20) , (6,19,100) , (2,100,200)] 
print(weightScheduling(sam))
