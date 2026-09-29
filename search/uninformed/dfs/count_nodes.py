def dfs_count(graph, node, visited):
    count = 0

    if node not in visited:
        count = count + 1
        visited.add(node)

        for neighbour in graph[node]:
            count = count + dfs_count(graph, neighbour, visited)

    return count

# Test-case
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

print('Number of nodes:', dfs_count(graph, '5', set()))