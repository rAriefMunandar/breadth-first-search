from collections import defaultdict, deque

# Definisi graf sebagai dictionary berisi kota-kota dan jarak antar kota
graph = {
    'A': {'B': 12, 'C': 8},
    'B': {'A': 12, 'C': 7, 'E': 15},
    'C': {'A': 8, 'B': 7, 'E': 25, 'D': 16},
    'D': {'C': 16, 'E': 9, 'F': 8},
    'E': {'B': 15, 'C': 25, 'D': 9, 'G': 11},
    'F': {'D': 8, 'G': 10},
    'G': {'E': 11, 'F': 10}
}

def bfs_shortest_path(graph, start, goal):
    # Queue untuk menyimpan simpul yang akan dikunjungi
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (current_node, path) = queue.popleft()
        for neighbor, distance in graph[current_node].items():
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                if neighbor == goal:
                    return path + [neighbor]

# Menggunakan BFS untuk mencari jarak terpendek dari A ke F
shortest_path = bfs_shortest_path(graph, 'A', 'F')

# Mencetak hasil
print("Jarak terpendek dari A ke F:", shortest_path)
