def main():
    y = int(input())
    ans = False
    if y%4==0:
        ans = True
    if y%100==0:
        ans = False
    if y%400==0:
        ans = True
    if ans:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
