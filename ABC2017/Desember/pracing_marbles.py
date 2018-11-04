def main():
    n=input()
    from collections import Counter
    c=Counter(list(n))
    print(c['1'])

if __name__=='__main__':
    main()
