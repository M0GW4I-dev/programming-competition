def main():
    from collections import Counter
    n,k=[int(i) for i in input().split()]
    c=Counter([int(i) for i in input().split()])
    key=sorted(c,key=lambda x:c[x])
    ans=0
    if len(c)-k <=0:
        print("0")
    else:
        for i in key[:len(c)-k]:
            ans+=c[i]
        print(ans)

if __name__=='__main__':
    main()

    

