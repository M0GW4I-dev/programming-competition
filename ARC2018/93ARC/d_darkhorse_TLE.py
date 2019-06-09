from itertools import permutations


def main():
    n,m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    p = permutations([i for i in range(1,2**n+1)])
    ans = 0
    for pp in p:
        breakFlag = False
        pp = list(pp)
        while len(pp) != 1:
            tmp = []
            for i in range(0,len(pp)-1,2):
                if pp[i] in a and pp[i+1] == 1:
                    if pp[i+1] == 1:
                        breakFlag = True
                        break
                    tmp.append(i+1)
                elif pp[i+1] in a and pp[i] == 1:
                    if pp[i] == 1:
                        breakFlag = True
                        break
                    tmp.append(i)
                elif not pp[i] in a and pp[i+1] == 1:
                    if pp[i] == 1:
                        breakFlag = True
                        break
                    tmp.append(i)
                elif not pp[i+1] in a and pp[i] == 1:
                    if pp[i+1] == 1:
                        breakFlag = True
                        break
                    tmp.append(i+1)
                elif pp[i]<pp[i+1]:
                    if pp[i+1] == 1:
                        breakFlag = True
                        break
                    tmp.append(i+1)
                else:
                    if pp[i] == 1:
                        breakFlag = True
                        break
                    tmp.append(i)
            if breakFlag:
                break
            tmp.reverse()
            for tt in tmp:
                del pp[tt]
            if len(pp) == 1:
                if pp[0] == 1:
                    ans += 1
                    break
                else:
                    break
        print(ans)
        if breakFlag:
            continue
    print(ans)

if __name__ == '__main__':
    main()







