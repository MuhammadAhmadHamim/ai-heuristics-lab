graph = { 
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

def bfs_real_path(visited, graph, start, goal):
    visited.add(start)
    queue = [start]
    parent = {start: None} # Tracking the nodes through their parents
    while queue:
        current = queue.pop(0)
        
        if current == goal:
            path = []
            
            while current is not None:
                path.append(current)
                current = parent[current] # Move to it's parent
            path.reverse()
            
            return path
        
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = current # Assign parent to neighbour
                queue.append(neighbour)
    return None

# Test-case
print(bfs_real_path(set(), graph, '5', '8'))
