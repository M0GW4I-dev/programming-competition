def main():
    a = [int(input()) for i in range(5)]
    a.sort(key=lambda x: x%10 if x%10 != 0 else 10, reverse=True)
    ans = 0
    for aa in a[:4]:
        if aa%10 != 0:
            ans += aa+(10-aa%10) 
        else:
            ans += aa
    ans += a[4]
    print(ans)


if __name__ == '__main__':
    main()
