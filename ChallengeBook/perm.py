perm=[0,0,0]
used=[False,False,False]
array=['5','2','3']

def permutation(pos,n):
    if(pos==n):
        print(" ".join([array[i] for i in perm]))
        return
    for i in range(n):
        if not used[i]:
            perm[pos]=i
            used[i]=True
            permutation(pos+1,n)
            used[i]=False
    return

def main():
    permutation(0,3)

if __name__ == '__main__':
    main()




