def main():
    n = int(input())
    v = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        if v[i]-c[i] > 0:
            ans += v[i]-c[i]
    print(ans)

if __name__ == '__main__':
    main()
    