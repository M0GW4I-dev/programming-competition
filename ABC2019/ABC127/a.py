def main():
    a,b = [int(i) for i in input().split()]
    if 13 <= a:
        print(b)
    elif 6 <= a <= 12:
        print(b//2)
    else:
        print(0)

if __name__ == '__main__':
    main()
