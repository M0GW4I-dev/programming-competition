def main():
    n=int(input())
    s=input()
    rank={'A':4,'B':3,'C':2,'D':1,'F':0}
    res=0
    for i in s:
        res+=rank[i]
    print(res/n)

if __name__ == '__main__':
    main()
