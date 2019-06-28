# Dijkstra Algorithm: To solve single source shortest path problem
# (하나의 정점으로부터 다른 모든 정점까지의 최단 경로)

# Without Priority Queue: O(V^2)
# With Priority Queue: O(E + VlogV)

import heapq


class Graph():
    def __init__(self, vertices):
        self.vertices = {}

        for v in vertices:
            self.vertices[v] = []

    def add_edge(self, _from, to, weight):
        self.vertices[_from].append((to, weight))

    def edges_from(self, vertex_name):
        return self.vertices[vertex_name]

    def get_vertices(self):
        return self.vertices.keys()


class PriorityQueue():
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def push(self, vertex, length):
        heapq.heappush(self.queue, (length, vertex))

    def pop(self):
        return heapq.heappop(self.queue)[1]


def get_vertex_of_shortest_path(shortest_paths, to_visit):
    min_path_length = 10000
    min_index = ''

    for v in to_visit:
        if shortest_paths[v] < min_path_length:
            min_path_length = shortest_paths[v]
            min_index = v

    return min_index


def dijkstra(graph, start_vertex):
    shortest_paths = {}

    # initialize
    for v in graph.get_vertices():
        if v == start_vertex:
            shortest_paths[v] = 0
        else:
            shortest_paths[v] = 10000

    to_visit = PriorityQueue()
    to_visit.push(start_vertex, shortest_paths[v])

    while len(to_visit) > 0:
        v = to_visit.pop()

        for next_v, weight in g.edges_from(v):
            if weight + shortest_paths[v] < shortest_paths[next_v]:
                shortest_paths[next_v] = weight + shortest_paths[v]
                to_visit.push(next_v, shortest_paths[next_v])

    return shortest_paths


if __name__ == '__main__':
    g = Graph(['1', '2', '3', '4', '5'])

    g.add_edge('1', '3', 6)
    g.add_edge('1', '4', 3)
    g.add_edge('2', '1', 3)
    g.add_edge('3', '4', 2)
    g.add_edge('4', '2', 1)
    g.add_edge('4', '3', 1)
    g.add_edge('5', '2', 4)
    g.add_edge('5', '4', 2)

    print(dijkstra(g, '5'))
