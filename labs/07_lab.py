# Artificial Intelligence
# Lab 7

# Distances between cities
distance = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'C': 1},
    'C': {'A': 2, 'B': 1}
}

def tour_distance(tour):
    total = 0
    for i in range(len(tour) - 1):
        total = total + distance[tour[i]][tour[i+1]]

    return total

def hill_climbing():
    current = ['A', 'B', 'C']
    current_distance = tour_distance(current)

    print('Current:', current)
    print('Current distance:', current_distance)

    neighbour = ['A', 'C', 'B']
    neighbour_distance = tour_distance(neighbour)

    print('Neighbour:', neighbour)
    print('Neighbour distance:', neighbour_distance, 'km')
    
    if current_distance > neighbour_distance:
        current = neighbour
        current_distance = neighbour_distance

    return current, current_distance

best, best_distance = hill_climbing()

print('Best:', best)
print('Best distance:', best_distance)
