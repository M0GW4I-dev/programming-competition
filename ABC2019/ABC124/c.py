# シマシマ模様にしたい

def main():
    s = input()
    tmp = '0'
    ans = 0
    for i in range(len(s)):
        if tmp == '0':
            if s[i] != '0':
                ans += 1
            tmp = '1'
        else:
            if s[i] != '1':
                ans += 1
            tmp = '0'
    tmp = '1'
    ans2 = 0
    for i in range(len(s)):
        if tmp == '0':
            if s[i] != '0':
                ans2 += 1
            tmp = '1'
        else:
            if s[i] != '1':
                ans2 += 1
            tmp = '0'
    print(min(ans, ans2))


if __name__ == '__main__':
    main()
