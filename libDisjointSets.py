# https://youtu.be/ID00PMy0-vE

# Definition for a set node.
class TreeNode:
    def __init__(self, x: int):
        self.data: int = x

        self.rank: int = 0
        self.parent: TreeNode = None


class DisjointSets:
    def __init__(self):
        self.map = {}

    def make_set(self, x: int) -> None:
        if x not in self.map:
            self.map[x] = TreeNode(x)

    def merge_set(self, node_1: TreeNode, node_2: TreeNode):
        node_2.parent = node_1
        if node_2.rank == node_1.rank:
            node_1.rank += 1

    def union_int(self, node_1: int, node_2: int) -> None:
        self.union(self.map[node_1], self.map[node_2])

    def union(self, node_1: TreeNode, node_2: TreeNode) -> None:
        node_1 = self.find_set(node_1)
        node_2 = self.find_set(node_2)

        if node_1 == node_2:
            return

        if node_1.rank >= node_2.rank:
            self.merge_set(node_1, node_2)
        else:
            self.merge_set(node_2, node_1)

    def find_set_int(self, node: int) -> int:
        return self.find_set(self.map[node]).data

    def find_set(self, node: TreeNode) -> TreeNode:
        if node.parent is None:
            return node

        if node.parent.parent is not None:
            parent = self.find_set(node.parent)
            node.parent = parent

        return node.parent
