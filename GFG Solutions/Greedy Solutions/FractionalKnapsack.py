def FractionalKnapsack(sam):
    w = sam[1]
    sam = sam[0]
    sam.sort(key = lambda x : x[0] / x[1])
    print(sam)
    final = []
    
    for i in range(len(sam) - 1 , -1 , -1):
        if w == 0:
            break
        
        if w >= sam[i][1]:
            final.append(sam[i][0])
            w -= sam[i][1]
        
        else:
            final.append(sam[i][0] * (w / sam[i][1]))
            w = 0
            
    print(sum(final))
    return final        


sam1 = ([(5,1) , (10,3) , (15,5) , (7,4) , (8,1) , (9,3) , (4,2)] , 15)
sam2 = ([(60 , 10) , (100,20) , (120,30)] , 50)
sam3 = ([(60 , 10) , (100 , 20)] , 50)
print(FractionalKnapsack(sam3))
