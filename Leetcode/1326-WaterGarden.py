def watergarden(sam , n):
    final = 0
    l = r = 0
    
    while r < n:
        for i in range(len(sam)):
            if i - sam[i] <= l and i + sam[i] > r:
                r = i+sam[i]
        
        if l == r:
            return -1
        
        l = r
        final += 1
    return final    

sam = [3,4,1,1,0,0]
print(watergarden(sam , 5))
