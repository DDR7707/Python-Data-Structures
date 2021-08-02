def largestNum(n,s):
        
        final = []
        
        for i in range(n):
            if s >= 9:
                final.append(9)
                s = s - 9
            else:
                final.append(s)
                s = 0
            
        if s != 0:
            return -1
        
        return  "".join(map(str,final))  

print(largestNum(5,12))
