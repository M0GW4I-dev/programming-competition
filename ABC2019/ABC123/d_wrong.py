def main():
    x, y, z, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    ans = []
    for aa in a:
        for bb in b:
            for cc in c:
                ans.append(aa+bb+cc)
    ans.sort(reverse=True)
    for aa in ans[:k]:
        print(aa)


if __name__ == '__main__':
    main()
