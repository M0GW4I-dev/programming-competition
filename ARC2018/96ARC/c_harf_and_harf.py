def main():
    a,b,c,x,y = [int(i) for i in input().split()]
    ans = 1 << 32
    if x < y:
        tmp = 2*x*c
        tmp += (y-x)*b
        ans = min(tmp,ans)
    else:
        tmp = 2*y*c
        tmp += (x-y)*a
        ans = min(tmp,ans)
    if a//2+b//2 < c:
        ans = x*a+ y*b
    ans=min(ans,2*max(x,y)*c)
    print(ans)

if __name__ == '__main__':
    main()

    
