def main():
    n = int(input())
    s = list(input())
    w = 0
    e = 0
    ans = 1<<32
    for ss in s:
        if ss=="W":
            w+=1
        else:
            e+=1
    ww = 0
    for ss in s:
        if ss=="W":
            w -= 1
            ans = min(ans,e+ww)
            ww += 1
        else:
            e -= 1
            ans = min(ans,e+ww)
    print(ans)


if __name__ == '__main__':
    main()
