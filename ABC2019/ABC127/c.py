def main():
    n, m = [int(i) for i in input().split()]
    l_max, r_min = 0, 10**6
    for i in range(m):
        l, r = [int(j) for j in input().split()]
        l_max = max(l, l_max)
        r_min = min(r+1, r_min)
    if r_min-l_max <= 0:
        print(0)
    else:
        print(r_min-l_max)


if __name__ == '__main__':
    main()
