def catchThieves(arr, n, k): 
        t = []
        p = []
        final = 0
        
        for i in range(n):
            if arr[i] == "T":
                t.append(i)
            else:
                p.append(i)
        
        print(t , p)
        l = r = 0
        
        while l < len(t)  and r < len(p):
            if abs(t[l] - p[r]) <= k:
                final += 1
                l += 1
                r += 1
                
            elif  p[r] > t[l]:
                l += 1
            
            elif p[r] < t[l]:
                r += 1
                
        return final 

        
arr = ["P" , "T" , "T" , "P" , "T"]
print(catchThieves(arr , 5 , 1))
