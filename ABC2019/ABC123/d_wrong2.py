# 落ちるわ
def main():
    x, y, z, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    ab = []
    for aa in a:
        for bb in b:
            ab.append(aa+bb)
    ab.sort(reverse=True)
    abc = []
    for i in range(min(k,len(ab))):
        for j in range(len(c)):
            abc.append(ab[i]+c[j])
    abc.sort(reverse=True)
    for i in range(k):
        print(abc[i])


if __name__ == '__main__':
    main()
