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