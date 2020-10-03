from typing import List


class TreeNode:
    def __init__(self, x):
        self.name = x
        self.last_child = None

        self.alive = True

        self.left = None
        self.right = None


def insert_into_inheritance(last_child, child):
    temp_right = last_child.right

    last_child.right = child
    child.left = last_child

    child.right = temp_right


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.cur_king = TreeNode(kingName)
        self.family_map = {kingName: self.cur_king}

    def birth(self, parentName: str, childName: str) -> None:
        child = TreeNode(childName)

        parent = self.family_map[parentName]

        last_child = parent
        while last_child.last_child is not None:
            last_child = last_child.last_child

        insert_into_inheritance(last_child, child)

        self.family_map[childName] = child
        parent.last_child = child

    def death(self, name: str) -> None:
        child = self.family_map[name]
        child.alive = False

        if self.cur_king == child:
            self.cur_king = self.cur_king.right

    def getInheritanceOrder(self) -> List[str]:
        head = self.cur_king

        ans = []
        while head is not None:
            if head.alive:
                ans.append(head.name)
            head = head.right
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
obj = ThroneInheritance("king")
print(obj.getInheritanceOrder())

obj.birth("king", "andy")
print(obj.getInheritanceOrder())
obj.birth("andy", "matthew")
print(obj.getInheritanceOrder())

obj.birth("king", "bob")
print(obj.getInheritanceOrder())
obj.birth("bob", "alex")
print(obj.getInheritanceOrder())

obj.birth("king", "catherine")
print(obj.getInheritanceOrder())

obj.birth("bob", "asha")
print(obj.getInheritanceOrder())

obj.death("bob")
print(obj.getInheritanceOrder())
