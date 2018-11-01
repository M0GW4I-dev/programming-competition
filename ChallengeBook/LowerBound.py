def main():
    n,k = [int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    lb=-1
    ub=n
    while ub-lb>1:
        mid=(lb+ub)//2
        if a[mid]>=k:
            ub=mid
        else:
            lb=mid
    print(ub)

if __name__ == '__main__':
    main()

