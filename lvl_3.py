def bfs(graph, v):
    visited = {v}
    to_explore = [v]
    while to_explore:
        u = to_explore.pop(0)
        print(u)
        new_vertices = [i for i in graph[u] if i not in visited]
        to_explore.extend(new_vertices)
        visited.update(new_vertices)


graph = {
    1: [2, 8],
    2: [1, 3, 8],
    3: [2, 4, 8],
    4: [3, 7, 9],
    5: [6, 7],
    6: [5],
    7: [4, 5, 8],
    8: [1, 2, 3, 7],
    9: [4],
}

print(graph)
v = int(input("Введите номер вершины: "))
bfs(graph, v)
