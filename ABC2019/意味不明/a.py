def main():
    a = []
    flag = False
    for i in range(5):
        a.append(int(input()))
    k = int(input())
    for i in a:
        for j in a:
            if i - j > k:
                print(':(')
                flag = True
                break
        if flag:
            break
    else:
        print('Yay!')


if __name__ == '__main__':
    main()


