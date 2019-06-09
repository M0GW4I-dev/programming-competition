""" MNlogN でTLE """
import heapq

def main():
    n,m = [int(i) for i in input().split()]
    heap = [int(i) for i in input().split()]
    heap.sort()
    for i in range(m):
        b, c = [int(j) for j in input().split()]
        counter = 0
        while heap[0] < c and counter < b:
            heapq.heappop(heap)
            heapq.heappush(heap, c)
            counter += 1
    print(sum(heap))


if __name__ == '__main__':
    main()
