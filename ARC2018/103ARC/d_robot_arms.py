def solve(xy):
    p = False
    if all([(x+y)%2==0 for x,y in xy]):
        p = True
    elif all([(x+y)%2==1 for x,y in xy]):
        pass
    else:
        print(-1)
        return
    m = [2**i for i  in range(30,-1,-1)]
    if p:
        m.append(1)
    anses = []
    for x,y in xy:
        usum, vsum = (0, 0)
        ans = []
        u = x+y
        v = x-y
        anses.append(ans)
        for d in m:
            if usum <= u:
                usum += d
                if vsum <= v:
                    vsum += d
                    ans.append('R')
                else:
                    vsum -= d
                    ans.append('U')
            else:
                usum -= d
                if vsum <= v:
                    vsum += d
                    ans.append('D')
                else:
                    vsum -= d
                    ans.append('L')
    print(len(m))
    print(" ".join([str(i) for i in m]))
    for a in anses:
        print("".join(a))
        

def main():
    n = int(input())
    xy = []
    for i in range(n):
        xy.append([int(i) for i in input().split()])
    solve(xy)

if __name__ == '__main__':
    main()

