def main():
    n, y = [int(i) for i in input().split()]
    sw1 = False
    for i in range(n+1):
        for j in range(n-i+1):
            if 10000 * i + 5000 * j + 1000 * (n-i-j) == y:
                sw1 = True
                print(i, j, n-j-i)
                break
        if sw1:
            break
    else:
        print(-1, -1, -1)

if __name__ == '__main__':
    main()


