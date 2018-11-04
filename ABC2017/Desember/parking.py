def main():
    n,a,b=[int(i) for i in input().split()]
    ans=min(n*a,b)
    print(ans)

if __name__=='__main__':
    main()
