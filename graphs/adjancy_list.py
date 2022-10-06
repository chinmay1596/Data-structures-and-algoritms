class Graph:
    graph_dict = {}

    @classmethod
    def add_edge(cls, u, v, direction):
        # direction = 0 undirected
        # direction = 1 directed graph

        # create an edge from u to v
        if u in cls.graph_dict:
            cls.graph_dict[u].append(v)
        else:
            cls.graph_dict[u] = [v]
        if direction == 0:
            if v in cls.graph_dict:
                cls.graph_dict[v].append(u)
            else:
                cls.graph_dict[v] = [u]


if __name__ == '__main__':
    obj = Graph()

    n = int(input("Enter the number of nodes"))
    m = int(input("Enter the number of edges"))

    for i in range(m):
        u, v = map(int, input().split())
        obj.add_edge(u, v, 0)
    print(obj.graph_dict)
