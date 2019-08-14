def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    sw = 0
    alice = 0
    bob = 0
    for i in a:
        if sw == 0:
            alice += i
            sw = 1
        else:
            bob += i
            sw = 0
    print(alice-bob)

if __name__ == '__main__':
    main()


