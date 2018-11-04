def main():
    n=int(input())
    ss=[]
    for i in range(n):
        ss.append(input())
    ss.sort(key=lambda x:"".join(reversed(x)))
    for i in ss:
        print(i)

if __name__=='__main__':
    main()
