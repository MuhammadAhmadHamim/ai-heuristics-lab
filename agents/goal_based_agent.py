def dfs_path(graph, node, goal, path, visited):
    if node not in visited:
        visited.add(node)
        path.append(node)

        if node == goal:
            return path

        for neighbour in graph[node]:
            result = dfs_path(graph, neighbour, goal, path, visited)

            if result is not None:
                return result
        
        path.pop()
        
    return None


class goalAgent:
    def __init__(self, graph, start, goal):
        self.plan = None
        self.graph = graph
        self.start = start
        self.goal = goal
    
    def program(self):
        if self.plan is None:
            self.plan = dfs_path(self.graph, self.start, self.goal, [], set())

            if self.plan is None:
                return ('Goal not found!')
            
            self.plan.pop(0)

        if len(self.plan) == 0:
            return ('Goal reached!') 
        
        step = self.plan.pop(0)
        return ('Move to ' + step)

# Test-cases
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

# 1. Normal case — goal is reachable, a few hops away
agent = goalAgent(graph, '5', '4')
print(agent.program())
print(agent.program())

# 2. Start equals goal — the zero-length-path edge case
agent2 = goalAgent(graph, '5', '5')
print(agent2.program())

# 3. Goal unreachable — node exists in the graph, but no path leads to it
agent3 = goalAgent(graph, '8', '2')
print(agent3.program())

# 4. Goal isn't in the graph at all
agent4 = goalAgent(graph, '5', '99')
print(agent4.program())
