import math
def main():
    n,k = [int(i) for i in input().split()]
    ans = 0.0
    for i in range(1, n+1):
        # 出目
        if k <= i:
            # 出目がすでに k 以上の時
            ans += 1/n
        else:
            # それ以外
            ans += 1/n*(1/2)**math.ceil(math.log2(k/i))
    print(ans)

if __name__ == '__main__':
    main()
