
def gcd(x, y):
    xx = 0; yy = 0
    if x >= y:
        xx = x; yy = y
    else:
        xx = y; yy = x
    while yy > 0:
        xx, yy = yy, xx%yy
    return xx


def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    # i を入れた場合のgcdと i を入れない場合のgcdを考える
    ans = 1
    # gcd の結合則を利用する(X, Y, Zがありgcd(gcd(x,y),z)==gcd(x,gcd(x, y)))
    l = [0 for i in range(n)]
    r = [0 for i in range(n+1)]
    for i in range(n-1):
        l[i+1] = gcd(l[i], a[i])
    for i in range(n-1, -1, -1):
        r[i] = gcd(r[i+1],a[i])
    for i in range(n):
        ans = max(ans, gcd(l[i], r[i+1]))
    print(ans)


if __name__ == '__main__':
    main()
