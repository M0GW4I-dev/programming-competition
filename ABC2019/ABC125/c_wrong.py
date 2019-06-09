
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
    for i in range(n):
        tmp = -1
        for j in range(n):
            if j == i:
                continue
            if tmp == -1:
                tmp = a[j]
            tmp = gcd(tmp, a[j])
        ans = max(ans, tmp)
    print(ans)


if __name__ == '__main__':
    main()
