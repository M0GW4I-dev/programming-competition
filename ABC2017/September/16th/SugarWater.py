def main():
    a,b,c,d,e,f=[int(i) for i in input().split()]
    x=[]
    y=[]
    for i in range(f//(100*a)):
        for j in range(f//(100*b)):
            if 100*a+100*b <= f:
                x.append(100*a+100*b)
    lim=int(100*e/(100+e))
    for i in range(lim//c):
        for j in range(lim//d):
            if c*i+d*j <= lim:
                y.append(c*i+d*j)
    temp=0
    ans=[0,0]
    print(x,y)
    for i in x:
        for j in y:
            if temp<100*y/(x*y):
                ans = [i,j]
    print(ans[0],ans[1])

            


if __name__=='__main__':
    main()

