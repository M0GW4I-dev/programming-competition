""" bound.py for util binary search """
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

