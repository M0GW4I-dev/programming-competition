def main():
    n = int(input())
    x = [int(i) for i in input().split()]
    for i in range(len(x)):
        tmp = x[i]
        del x[i]
        newx = sorted(x)
        print(newx[len(newx)//2])
        x.insert(i, tmp)

if __name__ == '__main__':
    main()

