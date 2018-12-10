

def binsearch(x,value):
    left=0; right=len(x)-1
    if x[right] == value:
        return right
    elif x[left] == value:
        return left
    while True:
        m = (right+left)//2
        if x[m] == value:
            return m
        elif x[m] > value:
            right = m
        else:
            left = m


def main():
    n = int(input())
    x = [int(i) for i in input().split()]
    newx = sorted(x)
    for i in x:
        index = binsearch(newx,i)
        del newx[index]
        print(newx[(n-1)//2])
        newx.insert(index,i)


if __name__ == '__main__':
    main()

