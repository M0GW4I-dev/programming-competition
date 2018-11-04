def main():
    n,cc=[int(i) for i in input().split()]
    rec=[]
    for i in range(n):
        s,t,c=[int(k) for k in input().split()]
        rec.append([float(s),float(t),c])
    slot=[[float(-1),-1] for i in range(cc)]
    rec.sort(key=lambda rec:rec[0])
    for r in rec:
        for k,s in enumerate(slot):
            tmp=0
            if s[1]!=r[2]:
                #チャンネルが違う
                tmp=r[0]
                r[0]=r[0]-0.5
            if s[0]<=r[0]:
                s[0]=r[1]
                s[1]=r[2]
                break
            r[0]=tmp
    print(len([i for i in slot if i[0]!=-1 and i[1]!=-1]))

if __name__=='__main__':
    main()






