from collections import defaultdict
def main():
    n = int(input())
    s = input()
    d = defaultdict(int)
    for i in range(n):
        if i==n-1:
            break
        else:
            d[s[i]+s[i+1]]+=1
    keys = d.keys()
    MA = 0
    MK = None
    for k in keys:
        if MA < d[k]:
            MA = d[k]
            MK = k
    d = defaultdict(int)
    flag = 0
    for i in range(n):
        if i==n-1:
            break
        if flag == 1:
            flag = 0
            continue
        else:
            if s[i:i+2]==MK:
                flag = 1
                continue
            d[s[i:i+2]]+=1
    keys = d.keys()
    MB = 0
    MK = None
    for k in keys:
        if MB < d[k]:
            MB = d[k]
            MK = k
    print(n-MA-MB)

if __name__ == '__main__':
    main()




