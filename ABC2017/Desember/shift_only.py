def main():
    n=input()
    a=[int(i) for i in input().split()]
    ans=0
    f=False
    while True:
        for k,v in enumerate(a):
            if v%2==0:
                a[k]=a[k]//2
            else:
                print(ans)
                f=True
                break
        if f:
            break
        else:
            ans+=1

if __name__=='__main__':
    main()

