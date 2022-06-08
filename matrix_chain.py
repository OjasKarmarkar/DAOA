min_cost = float('inf')

p = [int(item) for item in input("Enter Matrices , Dimensions : ").split()]

n = len(p)

dp = [[0]*(n) for i in range (n)]
k_table = [[0]*(n) for i in range (n)]


def matrix_mult(p , dp):
    for L in range (2,n):

        for i in range(1,n - L + 1):

            j = i+L -1
            dp[i][j] = min_cost

            for k in range(i,j):
                c = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]

                if c<dp[i][j]:
                    dp[i][j] = c
                    k_table[i][j] = k
    return dp[1][n-1]

#Final Cost
print(matrix_mult(p ,dp))