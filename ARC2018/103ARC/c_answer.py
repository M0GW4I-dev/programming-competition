from collections import Counter


def main():
    n = int(input())
    v = [int(i) for i in input().split()]
    ans = 0
    odd = Counter(v[1::2])
    even = Counter(v[::2])
    odd_mosts = odd.most_common(2)
    even_mosts = even.most_common(2)
    if odd_mosts[0][0] == even_mosts[0][0]:
        if len(odd) == len(even) == 1:
            ans = n//2
        else:
            ans_sel = []
            ans_sel.append(n//2-odd_mosts[0][1]+n//2-even_mosts[1][1])
            ans_sel.append(n//2-odd_mosts[1][1]+n//2-even_mosts[0][1])
            ans = min(ans_sel)
    else:
        ans+=(n//2-odd_mosts[0][1])
        ans+=(n//2-even_mosts[0][1])
    print(ans)

if __name__ == '__main__':
    main()

