def bfs_count(graph, visited, start):
    q = []
    count = 0

    q.append(start)
    visited.add(start)

    while q:
        node = q.pop(0)
        count = count + 1

        for neighbour in graph[node]:
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)
    
    return count

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

print(bfs_count(state_space, set(), '1'))