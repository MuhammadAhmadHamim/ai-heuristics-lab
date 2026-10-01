def dfs_path(graph, node, goal, path, visited):
    if node not in visited:
        visited.add(node)
        path.append(node)

        if node == goal:
            print('Goal found!')
            return path

        for neighbour in graph[node]:
            result = dfs_path(graph, neighbour, goal, path, visited)

            if result is not None:
                return result

        path.pop()

    return None

# Test-case
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

print(dfs_path(graph, '5', '8', [], set()))