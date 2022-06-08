a = input("Enter First text : ")
b = input("Enter Second text : ")
pattern = ''

dp = [[0 for __ in range(len(b)+1)] for _ in range(len(a)+1)]
pattern = ''

# Tabulation Bottom Up Approach (Construct Table )
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):

        if a[i-1] == b[j-1]:

            dp[i][j] = 1 + dp[i-1][j-1]
        else:

            dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    


#trace it back
i=len(a)
j=len(b)

while i>0 and j>0:

    if a[i-1] == b[j-1]:
        pattern+=a[i-1]
        i-=1
        j-=1
    
    elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
             
    else:
            j -= 1

print(dp[-1][-1])
print(pattern[::-1])
