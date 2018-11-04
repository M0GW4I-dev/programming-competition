def main():
    n=int(input())
    ans=[]
    ans.append(2)
    ans.append(1)
    for i in range(2,87):
        ans.append(ans[i-1]+ans[i-2])
    print(ans[n])

if __name__=='__main__':
    main()

        
