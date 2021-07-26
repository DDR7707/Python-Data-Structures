def greater_on_right(sam):
    stack = [0] * len(sam)
    ref = 0
    for i in range(len(sam) - 1 , -1 , -1):
        if ref == 0:
            stack[i] = -1
            ref = sam[i]
        
        elif sam[i] < ref:
            stack[i] = ref
        
        elif sam[i] > ref:
            stack[i] = -1
            ref = sam[i]
    return stack        
            
print(greater_on_right([3,4,20,6,15,2,1,7]))


def greater_immediate(sam):
    final = [0] * len(sam)
    stack = []
    
    for i in range(len(sam) - 1 , -1 , -1):
        while len(stack) > 0 and sam[i] >= stack[-1]:
            stack.pop()
            
        if len(stack) == 0:
            final[i] = -1
        
        else:
            final[i] = stack[-1]
        
        stack.append(sam[i])  
    return final    

print(greater_immediate([11,13,21,3])) 
