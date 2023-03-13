class Graph:
    def __init__(self, n, m):
        self.l = [[] for _ in range(n + 1)]

    def add_edge_undirected(self, u, v):
        self.l[u].append(v)
        self.l[v].append(u)

    def add_edge_directed(self, u, v):
        self.l[u].append(v)


if __name__ == '__main__':

    n = int(input("Enter the number of nodes"))
    m = int(input("Enter the number of edges"))

    obj = Graph(n, m)

    for i in range(m):
        u, v = map(int, input().split())
        obj.add_edge_undirected(u, v)
    print(obj.l)
