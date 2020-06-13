class TreeNode:
    def __init__(self, x: str, parent=None, child=None):
        self.val = x
        self.parent = parent
        self.child = child

class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = TreeNode(homepage)
        self.current = self.root 

    def visit(self, url: str) -> None:
        temp = TreeNode(url, parent=self.current)
        self.current.child = temp

        self.current = temp        

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.parent is None:
                break
            self.current = self.current.parent
        return self.current.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.child is None:
                break
            self.current = self.current.child
        return self.current.val        


# Your BrowserHistory object will be instantiated and called as such:
homepage="leetcode.com"
obj = BrowserHistory(homepage)
obj.visit("google.com")
obj.visit("facebook.com")
obj.visit("youtube.com")

print("facebook.com", obj.back(1) )
print("google.com", obj.back(1) )

print("facebook.com", obj.forward(1) )

obj.visit("linkedin.com")
print("linkedin.com", obj.forward(2) )

print("google.com", obj.back(2) )
print("leetcode.com", obj.back(7) )