def main():
    a = []
    for i in range(5):
        a.append(int(input()))
    b = []
    s = 0
    tmp = 0
    for i in a:
        if i%10 != 0:
            tmp = i + (10-i%10)
            b.append(10-i%10)
        else:
            tmp = i
            b.append(0)
        s += tmp
    print(s-max(b))

if __name__ == '__main__':
    main()


