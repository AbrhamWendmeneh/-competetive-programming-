n = int(input())
k = int(input())
graph = {}
for _ in range(k):
    operation, u, *args = map(int, input().split())
    if operation == 1: 
        v = args[0]
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    elif operation == 2: 
        if u in graph:
            print(' '.join(map(str, graph[u])))
        else:
            print()

