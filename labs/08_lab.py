# Artificial Intelligence
# Lab 8 (Lab Midterm)

'''
A courier must get from the Depot to a customer's Home.
The road map is stored as a dictionary: for every place, a dictionary of neighbouring places and the distance in km.
'''

roads = {
    'Depot':  {'Market': 4, 'School': 2},
    'Market': {'Depot': 4, 'Park': 5, 'Bank': 10},
    'School': {'Depot': 2, 'Park': 8, 'Clinic': 10},
    'Park':   {'Market': 5, 'School': 8, 'Home': 6},
    'Bank':   {'Market': 10, 'Home': 3},
    'Clinic': {'School': 10, 'Home': 2},
    'Home':   {'Park': 6, 'Bank': 3, 'Clinic': 2},
}

'''
Write a function bfs(graph, start, goal) that uses a list as a queue and returns the route as a list of places with the FEWEST stops. 
Visit the neighbours of a place in the order they appear in the dictionary.
'''

def bfs(graph, start, goal):
    q = []
    visited = set()
    path = []
    parent = {start: None}
    q.append(start)
    visited.add(start)

    while q:
        node = q.pop(0)
        path.append(node)

        if node == goal:
            print('Goal Found!')
            current = parent[node]
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                q.append(neighbour)
                parent[neighbour] = node
                visited.add(neighbour)

        path.pop()

    return None

path_with_fewest_steps = bfs(roads, 'Depot', 'Home')
print(path_with_fewest_steps)
