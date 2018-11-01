def main():
    n = int(input())
    m = int(input())
    mes = [int(i) for i in input().split()]
    for i in range(n):
        x,y = (0,0)
        for arm,d in zip(list(input()),mes):
            if arm == 'U':
                y += d
            elif arm == 'D':
                y -= d
            elif arm == 'L':
                x -= d
            else:
                x += d
        print(x,y)


if __name__ == '__main__':
    main()
    
