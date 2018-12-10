def main():
    num = [int(i) for i in input().split()]
    num.sort()
    ans = 0
    ans+=((num[2]-num[1])//2)
    num[1]+=(num[2]-num[1])//2*2
    ans+=((num[2]-num[0])//2)
    num[0]+=(num[2]-num[0])//2*2
    if not (num[0]==num[1] and num[1]==num[2] and num[0]==num[2]):
        ans += 2
    print(ans)

if __name__ == '__main__':
    main()



