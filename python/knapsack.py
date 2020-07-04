def knapscak(weights, values, maxWeight):
    n=len(weights)
    dp=[[0 for _ in range(maxWeight+1)] for x in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,maxWeight+1):
            if weights[i-1]<=j:
                dp[i][j]=max(dp[i-1][j], values[i-1]+dp[i-1][j-weights[i-1]])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print(knapscak(wt,val,W))