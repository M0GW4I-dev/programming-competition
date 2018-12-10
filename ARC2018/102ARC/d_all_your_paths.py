def ge(k,array,ind):
    return array[ind]>=k

def lower_bound(k, array, func=ge):
    """
    k 以上を満たす最小のインデックスを返す
    もしなかったら要素数を返す
    """
    lb=-1
    ub=len(array)
    while ub-lb>1:
        mid = (lb+ub)//2
        if func(k,array,mid):
            ub=mid
        else:
            lb=mid
    return ub

def lt(k,array,ind):
    return array[ind]<k

def upper_bound(k, array, func=lt):
    """
    k 未満を満たす最大のインデックスを返す
    もしなかったら-1を返す
    """
    lb=-1
    ub=len(array)
    while ub-lb>1:
        mid = (lb+ub)//2
        if func(k,array,mid):
            lb=mid
        else:
            ub=mid
    return ub-1
def main():
    l = int(input())
    ans = []
    array = [i for i in range(60)]
    ind = upper_bound(l, array, lambda k,array,mid:2**mid<=k)
    r = array[ind]
    n = r+1
    for i in range(1,n):
        ans.append((i,i+1,0))
        ans.append((i,i+1,2**(i-1)))
    for t in range(n-1,0,-1):
        if l-2**(t-1)>=2**r:
            ans.append((t,n,l-2**(t-1)))
            l-=2**(t-1)
    print(n,len(ans))
    for f,t,c in ans:
        print(f,t,c)

if __name__ == '__main__':
    main()

