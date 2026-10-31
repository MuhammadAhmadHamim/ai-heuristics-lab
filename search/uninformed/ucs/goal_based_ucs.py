import heapq

graph_w = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 5), ('B', 1), ('D', 1)],
    'D': [('B', 4), ('C', 1)]
}

def ucs(visited, graph, start, goal):
    frontier = [(0, start, [start])]
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        print('Expanding the node', node, 'with cost', cost)

        if node == goal:
            print('Goal found!')
            return path, cost
        
        if node in visited:
            continue
        
        visited.add(node)
        
        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                heapq.heappush(frontier, (cost + weight, neighbour, path + [neighbour]))
    return None, None

path, cost = ucs(set(), graph_w, 'A', 'D')
print("UCS path:", path, "cost:", cost)