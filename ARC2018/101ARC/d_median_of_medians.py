def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    m = []
    for l in range(0, len(a)):
        for r in range(l+1, len(a)+1):
            m.append(a[l:r][len(a[l:r])//2])
    m.sort()
    if len(m) == 1:
        print(m[len(m)//2])
    else:
        print(m[len(m)//2+1])
    

if __name__ == '__main__':
    main()
