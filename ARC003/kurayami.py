from collections import deque
ss=[]
def proceed(n,t,ans):
    global ss
    maximum=0
    ns=[]
    if ss[n[0]][n[1]]=='g':
        return ans
    ss[n[0]][n[1]]='#'
    for i in [[0,1],[0,-1],[1,0],[-1,0]]:
        if 0<=n[0]+i[0]<len(ss[0]) and 0<=n[1]+i[1]<len(ss) and ss[n[0]+i[0]][n[1]+i[1]]!='#':
            if ss[n[0]+i[0]][n[1]+i[1]]=='g':
                return ans
            maximum=max(maximum,int(ss[n[0]+i[0]][n[1]+i[1]]))
    for i in [[0,1],[0,-1],[1,0],[-1,0]]:
        if 0<=n[0]+i[0]<len(ss[0]) and 0<=n[1]+i[1]<len(ss) and ss[n[0]+i[0]][n[1]+i[1]]!='#':
            if int(ss[n[0]+i[0]][n[1]+i[1]])==maximum:
                ns.append([n[0]+i[0],n[1]+i[1]])
    minimum=10000
    for i in ns:
        minimum=min(minimum,proceed(i,t+1,min(ans,int(ss[i[0]][i[1]])*0.99**t)))
    return minimum
    
def main():
    global ss
    n,m=[int(i) for i in input().split()]
    start=None
    end=None
    for i in range(n):
        ss.append(list(input()))
        for s in enumerate(ss[i]):
            if s[1]=='s':
                start=[i,s[0]]
            elif s[1]=='g':
                end=[i,s[0]]
    ans=proceed(start,1,10000)
    print(ans)
    print(ss)
    
if __name__=='__main__':
    main()

    
