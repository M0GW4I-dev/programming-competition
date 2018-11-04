N = 100
weight_to_root = [ 0 for i in range(N)]
rank = [ 0 for i in range(N) ]
par = [ i for i in range(N)]


def find(x):
    if par[x] == x:
        return x
    else:
        root = find(par[x])
        weight_to_root[x] += weight_to_root[par[x]]
        return root

def union(x,y,w):
    a = find(x)
    b = find(y)
    if a == b:
        return
    w -= weight_to_root[x]
    w += weight_to_root[y]
    if rank[a]>rank[b]:
        weight_to_root[b]=w
        par[b]=a
    elif rank[a]<rank[b]:
        weight_to_root[a]=-w
        par[a]=b
    else:
        rank[a] += 1
        par[b] = a
        weight_to_root[b]=w
        
def diff(x,y):
    a=find(x)
    b=find(y)
    if a!=b:
        return "?"
    return weight_to_root[x]-weight_to_root[y]

def is_same(x,y):
    return find(x) == find(y)

def main():
    global weight_to_root,par,rank
    n,q = [int(i) for i in input().split()]
    weight_to_root = [ 0 for i in range(n)]
    par = [ i for i in range(n)]
    rank = [0 for i in range(n)]

    for i in range(q):
        s = [int(j) for j in input().split()]
        if s[0] == 0:
            union(s[1],s[2],s[3])
        else:
            print(diff(s[1],s[2]))

if __name__ == '__main__':
    main()


