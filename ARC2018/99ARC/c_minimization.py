import math

def main():
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    ans = math.ceil((n-1)/(k-1))
    print(ans)

if __name__ == '__main__':
    main()
        

