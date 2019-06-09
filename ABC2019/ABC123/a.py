def main():
    a = [int(input()) for i in range(5)]
    k = int(input())
    ans = False
    for aa in a:
        for b in a:
            if abs(aa-b) > k:
                ans = True
                break
        if ans:
            break
    print(':(' if ans else 'Yay!')

if __name__ == '__main__':
    main()