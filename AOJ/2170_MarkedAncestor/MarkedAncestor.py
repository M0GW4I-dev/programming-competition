import sys
sys.setrecursionlimit(1000000)
marked = []
par = []
rank = []

def find(x):
    if par[x] == x:
        return x
    else:
        if marked[x]:
            return x
        return find(par[x])

def main():
    global marked, par, rank
    n,q = [int(i) for i in input().split()]
    marked = [False for i in range(n+1)]
    par = [ i for i in range(n+1)]
    rank = [ 0 for i in range(n+1)]
    ans = 0
    for i in range(2,n+1):
        par[i] = int(input())
    for i in range(q):
        s = input().split()
        if s[0] == 'Q':
            print(find(int(s[1])))
        else:
            marked[int(s[1])]=True
    input()

if __name__ == '__main__':
    main()





