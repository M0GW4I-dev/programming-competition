def main():
    n, k = [int(i) for i in input().split()]
    s = input()
    s += 'N'
    # i は現在の文字
    # length は 0 が続いてる数
    # m_length は max(length)
    # is_zero
    # 0 が連続で続いている場所のリストのリスト
    c = []
    l, r = None, None
    for i in range(n):
        # 0 が連続しているところを探す
        if s[i] == '0' and l == None:
            l,r  = i, i
            if s[i+1] == 'N':
                c.append((l, r))
        elif s[i] == '0' and l != None:
            r = i
            if s[i+1] == 'N':
                c.append((l, r))
        else:
            # s[i] が '1'
            if l != None:
                c.append((l, r))
                l, r = None, None
    c.sort(key=lambda x: x[1]+1-x[0], reverse=True)
    c = c[:min(len(c), k)]
    c.sort(key=lambda x: x[0])
    print(c)
    # 数え上げ
    for cc in c:
        s = s[:cc[0]]+"".join(['1' for i in range(cc[1]+1-cc[0])])+s[cc[1]+1:]
    start = False
    print(s)
    length = 0
    ans = 0
    for i in range(n):
        if s[i] == '1' and s[i+1] == '1':
            length += 1
        elif s[i] == '1' and s[i+1] != '1':
            length += 1
            ans = max(ans, length)
            length = 0
    print(ans)


if __name__ == '__main__':
    main()
