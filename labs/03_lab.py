# Artificial Intelligence
# Lab 3

# Part A.1 Dictionaries
'''
fruit_colors = {'apple': 'red', 'banana':'yellow', 'grape':'purple'}
print(fruit_colors['apple'])
'''

# Part A.2 Lists
'''
neighbours = ['B', 'C']
for n in neighbours:
    print(n)
'''

# A.3 Sets
'''
visited = set()
visited.add('A')
print('A' in visited)
'''

# A.4 Functions and Recursion
'''
def countdown(n):
    if n == 0:
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)   # the function calls itself

countdown(3)
'''

# Part B - Graph and Trees, in Plain Terms
'''
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}
'''

# D.1 Plain DFS 
'''
visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
dfs(visited, graph, '5')
'''

# D.2 DFS With a Goal Test
'''
visited2 = set()

def dfs_goal(visited, graph, node, goal):
    if node not in visited:
        print(node)
        visited.add(node)

    if node == goal:
        print('Goal found!')
        return True

    for neighbour in graph[node]:
        if(dfs_goal(visited, graph, neighbour, goal)):
            return True
    return False

dfs_goal(visited2, graph, '5', '4')
'''

# Part E.Exercise 1
# Given fruit_colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'},
# print every fruit with its colour, one per line, in the format apple -> red
'''
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}

for name, color in fruit_colors.items():
    print(name, '->', color)
'''

# Part E.Exercise 2 — Build your own adjacency list
# Represent this graph as a Python dictionary:
# A connects to B and C; B connects to D; C connects to D; D connects to nothing.
'''
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

print(graph)
'''

# Part E.Exercise 4 — Count visited nodes instead of printing them
# Modify the plain DFS function so that instead of printing each node,
# it returns the total number of nodes visited.
'''
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()

def dfs_count(visited, graph, node):
    count = 0

    if node not in visited:
        count = count + 1
        visited.add(node)

        for neighbour in graph[node]:
            count = count + dfs_count(visited, graph, neighbour)

    return count

print(dfs_count(visited, graph, '5'))
'''

# Part E.Exercise 5 — Return the path instead of printing it
# Modify goal-based DFS so it returns the path taken (as a list),
# instead of only printing "Goal found!".
'''
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()

def dfs_path(visited, graph, node, goal, path):
    if node not in visited:
        visited.add(node)
        path.append(node)

        if node == goal:
            print('Goal found!')
            return path

        for neighbour in graph[node]:
            result = dfs_path(visited, graph, neighbour, goal, path)


            if result is not None:
                return result
        
        path.pop()
        
    return None

print(dfs_path(visited, graph, '5', '8', []))
# Use google scholar for the assignment
'''

# Part F - Graded Lab Tasks (for reference — solve these yourself)
# Solve the route-finding problem on the Romania road map using DFS, from Arad to Bucharest. Draw the graph, apply DFS, and report the path and total distance.

romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151),
              ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Pitesti', 138),
                ('Rimnicu Vilcea', 146)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146),
                       ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138),
                ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101),
                  ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98),
                 ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}


# Defined DFS for finding the path
'''
visited = set()

def dfs_path(visited, graph, node, goal, path):
    if node not in visited:
        visited.add(node)
        path.append(node)

        if node == goal:
            print('Goal found!')
            return path

        for neighbour, distance in graph[node]:
            result = dfs_path(visited, graph, neighbour, goal, path)


            if result is not None:
                return result
        
        path.pop()
        
    return None

print(dfs_path(visited, romania_map, 'Arad', 'Bucharest', []))    
'''

# DFS for the whole data
visited = set()

def dfs_data(visited, graph, node, goal, data):
    if node not in visited:
        visited.add(node)
        data['path'].append(node)

        if node == goal:
            print('Goal found!')
            return data

        for neighbour, distance in graph[node]:
            data['distance'] += distance
            result = dfs_data(visited, graph, neighbour, goal, data)


            if result is not None:
                return result

            data['distance'] -= distance
        data['path'].pop()
        
    return None

print(dfs_data(visited, romania_map, 'Arad', 'Bucharest', {'path': [],'distance': 0}))

'''
2. Generate all valid words from a 4x4 boggle board by searching in all eight directions, without reusing a cell.
3. Build the graph from the Romania map and find start/goal pairs where BFS visits fewer nodes than DFS, then find a pair where the opposite is true (this second part can be done after the next lab, once you've learned BFS).
'''
