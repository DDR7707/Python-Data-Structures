def kadanes(sam):
    max_sum = sam[0]
    comp = 0
    start = 0
    end = 0
    s = 0
    
    for i in range(len(sam)):
        
        comp += sam[i]
        
        if comp > max_sum:
            max_sum = comp
            start = s
            end = i
        
        elif comp < 0:
            comp = 0
            s = i + 1
            
    return max_sum , start , end  

sam = [-2,-3,4,-1,-2,1,5,-3]
print(kadanes(sam))
