def jumpgame2(sam):
    final = 0
    l = r = 0
    
    while r < len(sam)-1:
        maxi = 0
        for i in range(l,r+1):
            maxi = max(maxi , i + sam[i])
        
        l = r + 1
        r = maxi
        final += 1
    return final    

sam = [2,3,1,1,4]
print(jumpgame2(sam))
