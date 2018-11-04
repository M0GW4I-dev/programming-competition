def main():
    n=int(input())
    def luca(i):
        if i==0:
            return 2
        elif i==1:
            return 1
        else:
            return luca(i-1)+luca(i-2)
    print(luca(n))

if __name__=='__main__':
    main()

        
