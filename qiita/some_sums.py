def main():
    n, a, b = [int(i) for i in input().split()]
    ans = 0
    for i in range(1,n+1):
        tmp = 0
        for ss in str(i):
            tmp += int(ss)
        if a <= tmp <= b:
            ans += i
    print(ans)


if __name__ == '__main__':
    main()

