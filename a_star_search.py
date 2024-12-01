import heapq

class Node:
    def __init__(self, name, g=0, h=0):
        self.name = name
        self.g = g  # Cost from start to this node
        self.h = h  # Heuristic cost to goal
        self.f = g + h  # Total cost
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f


def a_star_search(graph, start, goal, heuristics):
    # Priority queue to store nodes for exploration
    open_list = []
    heapq.heappush(open_list, Node(start, g=0, h=heuristics[start]))
    
    # Closed list to track visited nodes
    closed_list = set()

    while open_list:
        # Get the node with the lowest f(n)
        current_node = heapq.heappop(open_list)

        # If goal is reached, reconstruct the path
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]
        
        closed_list.add(current_node.name)

        # Explore neighbors
        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_list:
                continue

            g_cost = current_node.g + cost
            h_cost = heuristics[neighbor]
            neighbor_node = Node(neighbor, g=g_cost, h=h_cost)
            neighbor_node.parent = current_node

            # Add neighbor to the open list
            heapq.heappush(open_list, neighbor_node)

    return None  # No path found


# Example usage
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 1, 'E': 5},
    'C': {'A': 3, 'F': 2},
    'D': {'B': 1, 'G': 9},
    'E': {'B': 5, 'G': 1},
    'F': {'C': 2, 'G': 1},
    'G': {}
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 6,
    'E': 2,
    'F': 1,
    'G': 0
}

start = 'A'
goal = 'G'
path = a_star_search(graph, start, goal, heuristics)

print(f"Shortest path from {start} to {goal}: {path}")
