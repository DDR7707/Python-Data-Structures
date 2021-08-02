def toyCount(N, K, arr):
        arr.sort()
        final = 0
        for i in arr:
            if K >= i:
                K -= i
                swap = False
                final += 1
            
        
        return final    

print(toyCount(7,50,[1, 12, 5, 111, 200, 1000, 10]))
