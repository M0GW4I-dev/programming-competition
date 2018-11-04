def isUru(y):
    ans = False
    if y%4==0:
        ans = True
    if y%100==0:
        ans = False
    if y%400==0:
        ans = True
    return ans

def main():
    y,m,d = [int(i) for i in input().split('/')]
    flag = False
    yy = y
    mm = m
    for dd in range(d,32):
        if yy%(mm*dd) == 0:
            if dd == 31 and mm in [2,4,6,9,11]:
                continue
            if mm == 2 and dd == 29 and not isUru(yy):
                continue
            if mm == 2 and dd == 30:
                continue
            print("{:04d}/{:02d}/{:02d}".format(yy,mm,dd))
            flag = True
            break
    if not flag:
        flag = False
        for mm in range(m+1,13):
            for dd in range(1,32):
                if yy%(mm*dd) == 0:
                    if dd == 31 and mm in [2,4,6,9,11]:
                        continue
                    if mm == 2 and dd == 29 and not isUru(yy):
                        continue
                    if mm == 2 and dd == 30:
                        continue
                    print("{:04d}/{:02d}/{:02d}".format(yy,mm,dd))
                    flag = True
                    break
            if flag == True:
                break

    if not flag:
        for yy in range(y+1,3001):
            for mm in range(1,13):
                for dd in range(1,32):
                    if yy%(mm*dd)==0:
                        if dd == 31 and mm in [2,4,6,9,11]:
                            continue
                        if mm == 2 and dd == 29 and not isUru(yy):
                            continue
                        if mm == 2 and dd == 30:
                            continue
                        print("{:04d}/{:02d}/{:02d}".format(yy,mm,dd))
                        flag = True
                        break
                if flag:
                    break
            if flag:
                break


if __name__ == '__main__':
    main()
