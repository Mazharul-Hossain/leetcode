# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        Solution: https://youtu.be/LR3K5XAWV5k
        """
        if root is None:
            return
        first_start_node, last_end_node = None, None
        previous_node = None

        # Set current to root of binary tree 
        current, previous_flag = root, False 
        while(current is not None): 
            if current.left is None: 
                previous_node = current
                previous_flag = True

                current = current.right 
            else: 
                # Find the previous of current 
                previous = current.left 
                while(previous.right is not None and previous.right != current): 
                    previous = previous.right 

                # Make curr as right child of its previous 
                if(previous.right is None): 
                    previous.right = current 
                    current = current.left 
                    
                # fix the right child of previous
                else: 
                    previous.right = None
                    previous_node = current 
                    previous_flag = True
                    
                    current = current.right 
            
            # Recover Binary Search Tree
            if previous_flag and current is not None and previous_node.val > current.val:
                if first_start_node is None:
                    first_start_node = previous_node
                last_end_node = current                
                previous_flag = False
                    
        if first_start_node is not None:
            temp = first_start_node.val
            first_start_node.val = last_end_node.val
            last_end_node.val = temp

# in-order traversal using stack 
def stack_inorder_traversal(root: TreeNode):
    # https://youtu.be/VsxLHGUqAKs
    node_stack = []    
    # Set current to root of binary tree
    current = root
    while(current is not None or len(node_stack) > 0):            
        if current is not None:    
            node_stack.append(current)
            current = current.left
        
        if current is None:
            stack_head = node_stack.pop()
            print(stack_head.val)
            current = stack_head.right

def morris_inorder_traversal(root: TreeNode):
    # https://youtu.be/wGXB9OWhPTg
    # https://www.educative.io/edpresso/what-is-morris-traversal
 
	# Set current to root of binary tree 
	current = root 
	while(current is not None): 
		if current.left is None: 
			print(current.val) 
			current = current.right 
		else: 
			# Find the previous of current 
			previous = current.left 
			while(previous.right is not None and previous.right != current): 
				previous = previous.right 

			# Make curr as right child of its previous 
			if(previous.right is None): 
				previous.right = current 
				current = current.left 
				
			# fix the right child of previous
			else: 
				previous.right = None
				print(current.val) 
				current = current.right 
			

# root = TreeNode(4) 
# root.left = TreeNode(2) 
# root.right = TreeNode(5) 
# root.left.left = TreeNode(1) 
# root.left.right = TreeNode(3) 

# Input: [1,3,null,null,2]
# root = TreeNode(1)
# root.left = TreeNode(3) 
# # root.right = TreeNode(5) 
# # root.left.left = TreeNode(1) 
# root.left.right = TreeNode(2) 

# print("calling morris_inorder_traversal: ")
# morris_inorder_traversal(root)

# Solution().recoverTree(root)

# print("calling morris_inorder_traversal: ")
# morris_inorder_traversal(root) 
# print("calling stack_inorder_traversal: ")
# stack_inorder_traversal(root)

# Input: [3,1,4,null,null,2]
root = TreeNode(3)
root.left = TreeNode(1) 
root.right = TreeNode(4) 
# root.left.left = TreeNode(1) 
# root.left.right = TreeNode(2) 
root.right.left = TreeNode(2)

print("calling morris_inorder_traversal: ")
morris_inorder_traversal(root)

Solution().recoverTree(root)

# print("calling morris_inorder_traversal: ")
# morris_inorder_traversal(root) 
print("calling stack_inorder_traversal: ")
stack_inorder_traversal(root)
