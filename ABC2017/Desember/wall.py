def main():
    h,w=[int(i) for i in input().split()]
    c=[]
    for i in range(10):
        c.append([int(i) for i in input().split()])
    for i in range(10):
        for j in range(10):
            for k in range(10):
                c[j][k]=min(c[j][k],c[j][i]+c[i][k])
    ans=0
    for i in range(h):
        for j in [int(k) for k in input().split()]:
            if j!=1 and j!=-1:
                ans+=int(c[j][1])
    print(ans)

if __name__=='__main__':
    main()

