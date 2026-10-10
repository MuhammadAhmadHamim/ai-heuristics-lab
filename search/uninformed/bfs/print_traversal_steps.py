def bfs_path(graph, visited, start, end):
    q = []
    path = []

    q.append(start)
    visited.add(start)
    

    while q:
        node = q.pop(0)
        path.append(node)

        if node == end:
            print("Goal Found!")
            return path

        for neighbour in graph[node]:
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)
    
    return 'Not found!'

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

print(bfs_path(state_space, set(), '1', '6'))