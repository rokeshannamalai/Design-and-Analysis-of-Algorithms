def kruskal_mst(edges):
    # Sort edges by weight
    edges = sorted(edges, key=lambda x: x[2])
    parent = {}

    def find(i):
        if i not in parent: parent[i] = i
        if parent[i] != i: parent[i] = find(parent[i])
        return parent[i]

    mst_cost = 0
    for u, v, w in edges:
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_u] = root_v
            mst_cost += w

    return mst_cost

# Test
edges = [(0,1,2), (1,2,3), (1,3,4), (2,3,5)]
print("MST Cost =", kruskal_mst(edges))
