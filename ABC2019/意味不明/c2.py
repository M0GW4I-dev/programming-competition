def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    dp = [[0 for i in range(10000)] for j in range(6)]
    dp[0][0]=n
    for i in range(6):
        for j in range(1,10000):
            dp[i][j] = max(dp[i][j], dp[i][j-1]-a)

