def main():
    n=input()
    a="Yes"
    if n[0]==n[1]==n[2]==n[3]:
        print("Yes")
    elif n[0]==n[1]==n[2]:
        print("Yes")
    elif n[3]==n[2]==n[1]:
        print("Yes")
    else:
        print("No")

if __name__=='__main__':
    main()
