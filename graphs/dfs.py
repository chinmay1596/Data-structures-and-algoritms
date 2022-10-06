class Solution:

    def dfs(self, node, vis, adj_list, store_dfs):
        store_dfs.append(node)
        vis[node] = True
        for i in range(len(adj_list.get(node))):
            if not vis[i]:
                self.dfs(i, vis, adj_list, store_dfs)

    def dfs_graph(self, v, adj_list):
        store_dfs = []
        vis = [v] * False

        for i in range(v):
            if not vis[i]:
                self.dfs(i, vis, adj_list, store_dfs)
        return store_dfs
