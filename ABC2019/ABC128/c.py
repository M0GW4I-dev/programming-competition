def main():
    n, m = [int(i) for i in input().split()]
    s = []
    # 接続グラフ
    # i 番目のスイッチには 電球との接続情報が入っている
    a = [0 for i in range(n)]
    for j in range(m):
        k, *switch = [int(i) for i in input().split()]
        for s in switch:
            a[s-1] |= (1 << j)
    p = int(("".join(reversed([i for i in input().split()]))), base=2)

    ans = 0
    # 全探索
    for i in range(1<<n):
        t = 0
        for j in range(n):
            if (i >> j & 1) == 1:
                t ^= a[j]
        if t == p:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()

