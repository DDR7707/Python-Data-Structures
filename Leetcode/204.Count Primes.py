def primes(n):
    
    dp = [1]*(n+1) 
    
    dp[0] = 0
    dp[1] = 0
    
    i = 2
    
    while i <= n:
        if dp[i]:
            j = i+i
            while j <= n:
                dp[j] = 0
                j += i
        i += 1
        
    return sum(dp)

print(primes(100))    
