def dfs_goal(graph, node, goal, visited):
    if node not in visited:
        print(node)
        visited.add(node)

    if node == goal:
        print('Goal found!')
        return True

    for neighbour in graph[node]:
        if(dfs_goal(graph, neighbour, goal, visited)):
            return True

    return False

# Test-case
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

print(dfs_goal(graph, '5', '4', set()))
