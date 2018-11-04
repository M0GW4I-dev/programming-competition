m = []
def rec(level,ans):
    global m
    if level==9:
        return True
    for k in range(8):
        for j in range(8):
            if m[k][j]==0:
                kk=[k,j]
                for i in range(8):
                    m[kk[0]][i]+=1
                    m[i][kk[1]]+=1
                    if 0<=kk[0]-i-1<=7 and 0<=kk[1]-i-1<=7:
                        m[kk[0]-i-1][kk[1]-i-1]+=1
                    if 0<=kk[0]+i+1<=7 and 0<=kk[1]-i-1<=7:
                        m[kk[0]+i+1][kk[1]-i-1]+=1
                    if 0<=kk[0]-i-1<=7 and 0<=kk[1]+i+1<=7:
                        m[kk[0]-i-1][kk[1]+i+1]+=1
                    if 0<=kk[0]+i+1<=7 and 0<=kk[1]+i+1<=7:
                        m[kk[0]+i+1][kk[1]+i+1]+=1
                m[kk[0]][kk[1]]-=1
                ret=rec(level+1,ans)
                if ret:
                    ans.append([k,j])
                    return ret
                for i in range(8):
                    m[kk[0]][i]-=1
                    m[i][kk[1]]-=1
                    if 0<=kk[0]-i-1<=7 and 0<=kk[1]-i-1<=7:
                        m[kk[0]-i-1][kk[1]-i-1]-=1
                    if 0<=kk[0]+i+1<=7 and 0<=kk[1]-i-1<=7:
                        m[kk[0]+i+1][kk[1]-i-1]-=1
                    if 0<=kk[0]-i-1<=7 and 0<=kk[1]+i+1<=7:
                        m[kk[0]-i-1][kk[1]+i+1]-=1
                    if 0<=kk[0]+i+1<=7 and 0<=kk[1]+i+1<=7:
                        m[kk[0]+i+1][kk[1]+i+1]-=1
                m[kk[0]][kk[1]]+=1
    return False


def main():
    global m
    k = []
    m = [[0 for i in range(8)] for j in range(8)]
    for i in range(8):
        s = list(input())
        for j in range(8):
            if s[j] == 'Q':
                k.append([i,j])
    ans = []
    flag = False
    for kk in k:
        for i in range(8):
            if m[kk[0]][kk[1]]!=0:
                    flag = True
                    break
            m[kk[0]][i]+=1
            m[i][kk[1]]+=1
            if 0<=kk[0]-i-1<=7 and 0<=kk[1]-i-1<=7:
                m[kk[0]-i-1][kk[1]-i-1]+=1
            if 0<=kk[0]+i+1<=7 and 0<=kk[1]-i-1<=7:
                m[kk[0]+i+1][kk[1]-i-1]+=1
            if 0<=kk[0]-i-1<=7 and 0<=kk[1]+i+1<=7:
                m[kk[0]-i-1][kk[1]+i+1]+=1
            if 0<=kk[0]+i+1<=7 and 0<=kk[1]+i+1<=7:
                m[kk[0]+i+1][kk[1]+i+1]+=1
        m[kk[0]][kk[1]]-=1
        if flag:
            break
    if not flag:
        ret = rec(4,ans)
    else:
        ret = False

    res = [['.' for i in range(8)] for j in range(8)] 
    if ret:
        for kk in k:
            res[kk[0]][kk[1]]='Q'
        for aa in ans:
            res[aa[0]][aa[1]]='Q'
        for i in res:
            print("".join(i))
    else:
        print("No Answer")

if __name__ == '__main__':
    main()



