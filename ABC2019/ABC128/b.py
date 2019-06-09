from collections import defaultdict


def main():
    n = int(input())
    d = defaultdict(list)
    for i in range(n):
        k, v = input().split()
        d[k].append((int(v), i+1))
    for k in sorted(d.keys()):
        for v in sorted(d[k], key=lambda x: x[0], reverse=True):
            print(v[1])

if __name__ == '__main__':
    main()
    

