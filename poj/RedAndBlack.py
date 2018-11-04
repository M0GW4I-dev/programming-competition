def main():
    w,h = [int(i) for i in input().split()]
    m = []
    ans = [0,]
    start = []
    for y in range(h):
        s = list(input())
        for x,c in enumerate(s):
            if c=='@':
                start = [y,x]
        m.append(s)
    dydx = [[0,1],[1,0],[0,-1],[-1,0]]
    def rec(nxt):
        m[nxt[0]][nxt[1]] = '#'
        ans[0] += 1
        for dy,dx in dydx:
            if 0 <= nxt[1]+dx < w and 0 <= nxt[0]+dy < h and m[nxt[0]+dy][nxt[1]+dx] == '.':
                rec([nxt[0]+dy,nxt[1]+dx])
    rec(start)
    print(ans[0])


if __name__ == '__main__':
    main()



        
        


        


