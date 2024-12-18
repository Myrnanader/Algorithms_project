class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(vertices, edges):
    # Sort edges based on their weight
    edges.sort(key=lambda x: x[2])  # x[2] is the weight of the edge

    uf = UnionFind(vertices)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        # Check if the current edge forms a cycle
        if uf.find(u) != uf.find(v):
            uf.union(u, v)  # Include this edge in the MST
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

# Example usage
if __name__ == "__main__":
    # Number of vertices
    vertices = 4
    # List of edges in the format (u, v, weight)
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    mst, total_weight = kruskal(vertices, edges)
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")
    print(f"Total weight of MST: {total_weight}")

    