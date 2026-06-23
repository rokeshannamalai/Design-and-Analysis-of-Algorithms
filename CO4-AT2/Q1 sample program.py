class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, set1, set2):
        root1, root2 = self.find(set1), self.find(set2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False

def kruskal_mst(locations, routes):
    # Sort by cost (Greedy Strategy)
    sorted_routes = sorted(routes, key=lambda x: x[2])
    uf = UnionFind(locations)
    mst, total_cost = [], 0
    
    for u, v, cost in sorted_routes:
        if uf.union(u, v):
            mst.append((u, v, cost))
            total_cost += cost
            if len(mst) == len(locations) - 1:
                break
    return mst, total_cost

# Quick Test
if __name__ == "__main__":
    locs = ["A", "B", "C", "D"]
    edges = [("A", "B", 5), ("B", "C", 10), ("A", "C", 15), ("C", "D", 2)]
    print(kruskal_mst(locs, edges)) # Output: ([('C', 'D', 2), ('A', 'B', 5), ('B', 'C', 10)], 17)
