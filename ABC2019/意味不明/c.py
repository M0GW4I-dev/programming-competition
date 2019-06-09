def main():
    n = int(input())
    a = []
    for i in range(5):
        a.append(int(input()))
    b = [n, 0, 0, 0, 0, 0]
    ans = 0
    while b[5] < n:
        for i in range(4, -1, -1):
            if b[i] > 0:
                if b[i] >= a[i]:
                    b[i] -= a[i]
                    b[i+1] += a[i]
                else:
                    tmp = b[i]
                    b[i] = 0
                    b[i+1] += tmp
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
