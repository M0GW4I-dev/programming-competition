

def main():
    s = input()
    k = int(input())
    substr = []
    for l in range(len(s)):
        for r in range(l+1,len(s)+1):
            if r-l > k:
                break
            substr.append(s[l:r])
    c=sorted(set(substr))

    print(c[k-1])


if __name__ == '__main__':
    main()

