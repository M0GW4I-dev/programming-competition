def main():
    s = input()
    s = "".join(reversed(s))
    word = ["dreamer", "dream", "eraser", "erase"]
    t = ""
    for i in range(4):
        word[i] = "".join(reversed(word[i]))
    while len(s) > 0:
        sw = False
        for i in range(4):
            if s.startswith(word[i]):
                s = s[len(word[i]):]
                sw = True
                break
        else:
            print("No")
            break
    if s == "":
        print("Yes")


if __name__ == '__main__':
    main()

