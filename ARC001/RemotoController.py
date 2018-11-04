def main():
    a,b = [int(i) for i in input().split()]
    c = 0
    if b-a>0:
        c = b-a
    else:
        c = a-b
    res=(c//10)
    c-=(c//10*10)
    if 5 < c < 10:
        res+=min(c-4,abs(c-10)+1)
    else:
        res+=min(c,abs(c-5)+1)
        
    print(res)

if __name__ == '__main__':
    main()

