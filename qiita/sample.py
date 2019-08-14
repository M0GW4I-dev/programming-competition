""" アイデアの解答 """

def main():
    n = int(input())
    r = []
    for i in range(n):
        rr, hh = [int(i) for i in input().split()]
        r.append([rr-hh, rr+hh])
    r.sort(key=lambda d: d[1])
    # i 番目の要素は i 番目のグループの右端の距離なかったら 0 のまま
    ans = [0 for i in range(n)]
    for s, e in r:
        for i in range(len(ans))
            if ans[i] < s:
                ans[i] = e
                break
    print(len([a != 0 for a in ans]))


if __name__ == '__main__':
    main()



