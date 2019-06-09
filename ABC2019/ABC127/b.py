def main():
    r, d, x = [int(i) for i in input().split()]
    for i in range(10):
        x = r * x - d
        print(x)

if __name__ == '__main__':
    main()
