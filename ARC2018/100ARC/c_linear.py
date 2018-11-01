def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    B = [a[i]-i-1 for i in range(len(a))]
    B.sort()
    ans = 0
    for i,aa in enumerate(a):
        ans+=abs(aa-(i+1)-B[len(B)//2])
    print(ans)


if __name__ == '__main__':
    main()
        

