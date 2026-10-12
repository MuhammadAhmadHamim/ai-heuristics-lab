# Artificial Intelligence
# Lab 5
'''
items = ['A', 'B', 'C']
heuristic_demo = {'A': 7, 'B': 5, 'C': 9}

best = min(items, key=lambda node: heuristic_demo[node])

print(best)

'''
# D.1 Activity 1 — Understanding the Effect of a Heuristic

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 5,
    'C': 3,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}

'''
def greedy_best_first(graph, heuristic, start, goal):
    frontier = [start]
    visited = set()

    while frontier:
        current = min(frontier, key=lambda node: heuristic[node])
        frontier.remove(current)
        print(current)

        if current == goal:
            print('Goal found!')
            return

        visited.add(current)

        for neighbour in graph[current]:
            if neighbour not in visited and neighbour not in frontier:
                frontier.append(neighbour)

greedy_best_first(graph, heuristic, 'A', 'G')
'''

# D.2 Activity 2 — Effect of Changing the Heuristic Function
'''
heuristic2 = {
    'A': 7,
    'B': 2,
    'C': 5,
    'D': 1,
    'E': 3,
    'F': 2,
    'G': 0
}

greedy_best_first(graph, heuristic2, 'A', 'G')
'''
# Exercise 1 — min() with key= warm-up
'''
Task: Given scores = [('Ali', 72), ('Sara', 88), ('Zain', 65)],
use min() with key= to find the entry with the lowest score.


scores = [('Ali', 72), ('Sara', 88), ('Zain', 65)]
lowest = min(scores, key=lambda pair: pair[1])

print(lowest)
print(lowest[0])
'''

# Exercise 3 — Return the path instead of printing it

gbfs_path(graph, heuristic, start, goal):
    frontier = [start]
    visited = set()
    parent = {start:None}

    while frontier:
        current = min(frontier, key=lambda node: heuristic[node])
        frontier.remove(current)
        if current == goal:

            while current:
                path.append(current)
                current = parent[current]

            path.reverse()
            return

        visited.add(current)
        for neighbour in graph[current]:
            if neighbour not in visited and neighbour not in frontier:
                parent[neighbour] = current
                frontier.append(neighbour)

    return None

print(gbfs_path(graph, heuristic, 'A', 'G'))


# Exercise 4 — Count how many nodes GBFS expands

def gbfs_count(graph, heuristic, start, goal):
    frontier = [start]
    visited = set()
    count = 0

    while frontier:
        current = min(frontier, key=lambda node: heuristic[node])
        frontier.remove(current)
        count += 1

        if current == goal:
            print('Goal found!')
            return count

        visited.add(current)

        for neighbour in graph[current]:
            if neighbour not in visited and neighbour not in frontier:
                frontier.append(neighbour)

    return count

print('Count:',gbfs_count(graph, heuristic, 'A', 'G'))

# Exercise 5 — Why GBFS Is Not Optimal
graph_trap = {
    'S': ['A', 'B'],
    'A': ['G'],
    'B': ['C'],
    'C': ['G'],
    'G': []
}

## Real costs (GBFS never looks at these — it only uses heuristic below)
costs = {('S','A'): 10, ('A','G'): 10, ('S','B'): 1, ('B','C'): 1, ('C','G'): 1}
heuristic_trap = {'S': 5, 'A': 1, 'B': 4, 'C': 2, 'G': 0}

path = gbfs_path(graph_trap, heuristic_trap, 'S', 'G')
print("GBFS path:", path)

def path_cost(path, costs):
    total = 0
    for i in range(len(path) - 1):
        total += costs[(path[i], path[i + 1])]
    return total

print("GBFS path cost:", path_cost(path, costs))
print("Alternative path cost:", path_cost(['S', 'B', 'C', 'G'], costs))

# Task 1 — Manhattan Distance as a Heuristic (worked)
def manhattan_distance(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

goal = (4, 4)
positions = [(0, 0), (1, 2), (2, 3), (3, 4), (4, 4)]
for p in positions:
    print(p, "->", manhattan_distance(p, goal))
