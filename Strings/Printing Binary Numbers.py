def binary(n):
    final = ["1"]
    look = ["1"]
    
    while len(final) < n:
        temp = look.pop(0)
        s1 = temp+"0"
        s2 = temp+"1"
        
        final.append(s1)
        if len(final) == n:
            break
        final.append(s2)
        
        look.append(s1)
        look.append(s2)
    
    return final    
        

print(binary(10))
