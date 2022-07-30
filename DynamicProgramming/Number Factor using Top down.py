def numberfactor(n,dp):
    
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        if n not in dp:
            sup1 = numberfactor(n-1,dp)
            sup2 = numberfactor(n-3,dp)
            sup3 = numberfactor(n-4,dp)
            dp[n] =  sup1 + sup2 + sup3
        return dp[n]

print(numberfactor(5,{}))