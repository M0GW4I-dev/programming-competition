from collections import deque


def main():
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    print(q[0])
    q.popleft()
    print(q[0])
    q.popleft()
    print(q[0])
    q.popleft()


if __name__ == '__main__':
    main()


