def main():
    a, b = [int(i) for i in input().split()]
    ans = max(a,b)
    ans += max(max(a,b)-1, min(a,b))
    print(ans)


if __name__ == '__main__':
    main()
