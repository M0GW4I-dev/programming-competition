def main():
    dp=[[0 for i in range(100+1)] for j in range(100+1)]
    a = input()
    b = input()
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    print(dp[len(a)][len(b)])


if __name__ == '__main__':
    main()

