from collections import Counter
def main():
    n = int(input())
    s = list(input())
    c = Counter(s)
    if len(c)!=4:
        res = 0
    else:
        res=min(c.values())

    print(max(c.values()),res)

if __name__=='__main__':
    main()

