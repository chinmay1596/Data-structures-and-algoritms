def bfs_graph(v, adj_list):
    bfs = []
    vis = []

    for i in range(len(v)):
        if not vis[i]:
            queue = []
            queue.append(i)
            vis[i] = True

            while len(queue) > 0:
                node = queue.pop(0)
                bfs.append(node)

                for i in range(len(adj_list.get(node))):
                    if not vis[i]:
                        vis[i] = True
                        queue.append(i)
    return bfs


# cycle detection in undirected graph

class Solution:
    def check_for_cycle(self, adj_list, node, vis):
        queue = []
        queue.append((node, -1))
        vis[node] = True

        while len(queue) > 0:
            data = queue.pop(0)
            first_node = data[0]
            prev_par = data[1]

            for i in adj_list.get(first_node):
                if not vis[i]:
                    queue.append((i, first_node))
                    vis[i] = True
                elif i != prev_par:
                    return True
        return False

    def is_cycle(self, v, adj_list):
        vis = [v] * False

        for i in range(v):
            if not vis[i]:
                if self.check_for_cycle(adj_list, i, vis):
                    return True
        return False
