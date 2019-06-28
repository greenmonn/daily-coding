# Dijkstra Algorithm: To solve single source shortest path problem
# (하나의 정점으로부터 다른 모든 정점까지의 최단 경로)


class Graph():
    def __init__(self, vertices):
        self.vertices = {}

        for v in vertices:
            self.vertices[v] = []

    def add_edge(self, _from, to, weight):
        self.vertices[_from].append((to, weight))

    def edges_to(self, vertex_name):
        return self.vertices[vertex_name]

    def get_vertices(self):
        return self.vertices.keys()


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

    to_visit = list(graph.get_vertices())[:]
    while len(to_visit) > 0:
        v = get_vertex_of_shortest_path(shortest_paths, to_visit)
        to_visit.remove(v)

        for next_v, weight in g.edges_to(v):
            shortest_paths[next_v] = min(
                shortest_paths[next_v], weight + shortest_paths[v])


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
