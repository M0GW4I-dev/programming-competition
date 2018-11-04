def main():
    n = int(input())
    s = input()
    ans = 10000
    for i in 'ABXY':
        for j in 'ABXY':
            flag=False
            for l in 'ABXY':
                for m in 'ABXY':
                    count=0
                    count2=0
                    if i+j != l+m:
                        for k in range(n):
                            if k==n-1:
                                break
                            if flag:
                                flag=False
                                continue
                            if s[k]+s[k+1] == i+j:
                                flag=True
                                count+=1
                            if s[k]+s[k+1] == l+m:
                                flag=True
                                count2+=1
                        ans = min(ans,n-count-count2)
    print(ans)

if __name__ == '__main__':
    main()




