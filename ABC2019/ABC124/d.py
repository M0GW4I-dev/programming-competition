def main():
    n, k = [int(i) for i in input().split()]
    s = [int(i) for i in list(input())]
    table = []
    now = 1
    cnt = 0
    for i in range(n):
        if s[i] == now:
            cnt += 1
        else:
            table.append(cnt)
            cnt = 1
            now ^= 1 # 0　と 1 の切り替え
    if cnt != 0:
        table.append(cnt)
    if len(table)%2 == 0:
        # 奇数で終わらせれば、1 で終わったことになる
        table.append(0)
    ans = 0
    l = 0
    d = min(len(table), 2*k+1)
    r = l + d
    tmp = sum(table[l:r])
    while r <= len(table):
        ans = max(ans, tmp)
        if l < len(table):
            tmp -= table[l]
        l += 1
        if l < len(table):
            tmp -= table[l]
        l += 1
        r += 1
        if r <= len(table):
            tmp += table[r-1]
        r += 1
        if r <= len(table):
            tmp += table[r-1]
    print(ans)


if __name__ == '__main__':
    main()
