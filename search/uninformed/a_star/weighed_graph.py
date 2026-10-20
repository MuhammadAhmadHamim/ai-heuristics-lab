graph = {
    'S': {'A': 1, 'B': 4, 'D': 2},
    'A': {'S': 1, 'B': 2},
    'B': {'S': 4, 'A': 2, 'C': 1},
    'C': {'B': 1, 'G': 3},
    'D': {'S': 2, 'G': 8},
    'G': {'C': 3, 'D': 8},
}

h = {'S': 6, 'A': 5, 'B': 4, 'C': 3, 'D': 7, 'G': 0}

def a_star(graph, h, start, goal):
    open_list = [(h[start], start)]
    g_cost = {start: 0}
    parent = {start: None}
    closed = set()

    while open_list:
        f, current = heapq.heappop(open_list)

        if current in closed:
            continue

        print(f"Expand {current}: g={g_cost[current]} h={h[current]} f={f}")

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1], g_cost[goal]

        closed.add(current)
        for nxt, cost in graph[current].items():
            new_g = g_cost[current] + cost 

            if nxt not in g_cost or new_g < g_cost[nxt]:
                g_cost[nxt] = new_g
                parent[nxt] = current
                heapq.heappush(open_list, (h[nxt] + new_g, nxt))

    return None, None

path, cost = a_star(graph, h, 'S', 'G')
print("Path:", path, "Cost:", cost)