def main():
    n,k = [int(i) for i in input().split()]
    candles = [int(i) for i in input().split()]
    i = 0
    res=1<<60;
    while i+k-1<n:
        left = candles[i]
        right = candles[i+k-1]
        res = min(res,min(abs(left),abs(right))+right-left)
        i+=1
    print(res)

if __name__ == '__main__':
    main()
