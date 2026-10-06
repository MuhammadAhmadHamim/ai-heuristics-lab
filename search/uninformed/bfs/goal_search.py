def bfs_goal(graph, visited, start, end):
    q = []

    q.append(start)
    visited.add(start)

    while q:
        node = q.pop(0)

        if node == end:
            return "Found!"

        for neighbour in graph[node]:
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)
    
    return "Not found!"

# Test-case(Tree)
state_space = {
    '1' : ['2','3','4'],
    '2' : ['5', '6'],
    '3' : [],
    '4' : ['7'],
    '5' : [],
    '6' : [],
    '7' : []
}

print(bfs_goal(state_space, set(), '1', '7'))