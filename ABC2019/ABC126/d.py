# TLEになった なんで
graph = []
n = 0
visited = []
ans = []

def dfs(v, ww):
    visited[v] = True
    ans[v] = ww
    for vv, w in enumerate(graph[v]):
        if w != -1 and not visited[vv]:
            dfs(vv, w+ww)
        

def main():
    global graph, n, visited, ans
    n = int(input())
    graph = [[-1 for i in range(n+1)] for j in range(n+1)]
    visited = [False for i in range(n+1)]
    ans = [0 for i in range(n+1)]
    for i in range(n-1):
        u, v, w = [int(j) for j in input().split()]
        graph[u][v] = w
    for i, _ in enumerate(visited):
        if visited[i] == False:
            dfs(i, 0)
    for i in range(len(ans)):
        if i == 0:
            continue
        print(ans[i]%2)


if __name__ == '__main__':
    main()
