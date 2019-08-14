from collections import Counter


def main():
    n = int(input())
    d = [int(input()) for i in range(n)]
    print(len(Counter(d)))

if __name__ == '__main__':
    main()


