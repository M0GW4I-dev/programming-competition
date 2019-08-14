def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    while all([aa%2 == 0 for aa in a]):
        ans += 1
        a = [aa//2 for aa in a]
    print(ans)


if __name__ == '__main__':
    main()

