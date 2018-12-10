# TLE
from math import factorial as fact
from itertools import combinations as comb


def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = [0,0]
    tmp = 0
    for i,j in comb(a,2):
        t = fact(max(i,j))//(fact(max(i,j)-min(i,j))*fact(min(i,j)))
        if tmp < t:
            ans = [max(i,j),min(i,j)]
            tmp = t
    print(ans[0],ans[1])


if __name__ == '__main__':
    main()







