from typing import List

# You can simply plug in this class any many different codes. This class is a generic implementation of union-find.
class UnionFind:
    # Initially all 'n' nodes are in different components.
    # e.g. component[2] = 2 i.e. node 2 belong to component 2.
    def __init__(self, n):
        self.component = []
        self.distinctComponents = n
        for i in range(n+1):
            self.component.append(i)

    # Returns true when two nodes 'a' and 'b' are initially in different
    # components. Otherwise returns false.
    def unite(self, a: int, b: int) -> bool:       
        if self.findComponent(a) != self.findComponent(b):
            self.component[self.findComponent(a)] = b
            self.distinctComponents -= 1
            return True        
        return False
    
    # Returns what component does the node 'a' belong to.
    def findComponent(self, a: int) -> int:
        if self.component[a] != a:
            self.component[a] = self.findComponent(self.component[a])
        return self.component[a]

    # Are all nodes united into a single component?
    def united(self) -> bool:
        return self.distinctComponents == 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Sort edges by their type such that all type 3 edges will be at the beginning.
        edges.sort(reverse=True)

        # Stores the number of edges added to the initial empty graph.
        edgesAdded = 0
        
        # Track whether bob and alice can traverse the entire graph,
        # are there still more than one distinct components, etc.
        alice, bob = UnionFind(n), UnionFind(n)
        
        # For each edge
        for edge in edges:
            type, one, two = edge

            if type == 3:
                edgesAdded += (bob.unite(one, two) | alice.unite(one, two))
            elif type == 2:
                edgesAdded += bob.unite(one, two)
            elif type == 1:
                edgesAdded += alice.unite(one, two)
                 
        if bob.united() and alice.united() :
            return len(edges) - edgesAdded
        else:
            return -1


obj = Solution()
print(2, obj.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
print(0, obj.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))
print(-1, obj.maxNumEdgesToRemove(n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]))