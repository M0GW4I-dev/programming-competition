import math
def main():
    k = int(input())
    a = [int(i) for i in input().split()]
    left=-1
    right=len(a)
    while right-left>1:
        print(a[left:right+1])
        mid=(right+left)//2
        if a[mid]<math.sqrt(k):
            left=mid
        else:
            right=mid
    print(a[left])

if __name__ == '__main__':
    main()
    
