def main():
    N=int(input())
    K=int(input())
    x=[int(i) for i in input().split()]
    ans=0
    for i in x:
        ans+=2*min(K-i,i)
    print(ans)

if __name__=='__main__':
    main()

