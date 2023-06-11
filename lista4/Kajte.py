import random
import heapq

# Implementacja klasy grafu
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def get_weight(self, u, v):
        return self.edges[u][v]
    
    def dijkstra(self, start, end):
        # Inicjalizacja odległości dla wszystkich wierzchołków jako "nieskończoność"
        distances = [float('inf')] * self.num_vertices
        distances[start] = 0

        # Inicjalizacja kolejki priorytetowej
        pq = [(0, start)]  # Krotka (odległość, wierzchołek)
        heapq.heapify(pq)

        # Inicjalizacja tablicy poprzedników
        predecessors = [-1] * self.num_vertices

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            # Przerywanie, jeśli osiągnęliśmy wierzchołek docelowy
            if current_vertex == end:
                break

            # Sprawdzanie sąsiadujących wierzchołków
            for neighbour in range(self.num_vertices):
                weight = self.get_weight(current_vertex, neighbour)
                if weight > 0:
                    distance = current_distance + weight

                    # Aktualizacja odległości, jeśli znaleziono krótszą ścieżkę
                    if distance < distances[neighbour]:
                        distances[neighbour] = distance
                        predecessors[neighbour] = current_vertex
                        heapq.heappush(pq, (distance, neighbour))

        # Odtworzenie najkrótszej ścieżki
        path = []
        current_vertex = end
        while current_vertex != -1:
            path.insert(0, current_vertex)
            current_vertex = predecessors[current_vertex]
        return_dist = 0
        for i in range(len(path)-1):
            return_dist = return_dist + self.get_weight(path[i],path[i+1])
        return return_dist

    
graph = Graph(6)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 2)
graph.add_edge(1, 3, 2)
graph.add_edge(1, 4, 3)
graph.add_edge(2, 4, 1)
graph.add_edge(3, 5, 3)
graph.add_edge(4, 5, 2)

shortest_path = graph.dijkstra(0, 5)
print(shortest_path)