from collections import defaultdict
def main():
    n,k = [int(i) for i in input().split()]
    group = defaultdict(list)
    ans = 0
    for i in range(1,n+1):
        group[i%k].append(i)
    ans += len(group[0])**3
    if k%2==0:
        ans += len(group[k//2])**3
    print(ans)


if __name__ == '__main__':
    main()



