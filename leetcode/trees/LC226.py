# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def invertTree(root):
        if root:
            root.right,root.left=root.left,root.right
            if root.right:
                invertTree(root.right)
            if root.left:
                invertTree(root.left)
        else:
            return None
        return root
        
def inOrder(root):
    if (root == None):
        return
    inOrder(root.left)
    print(root.val, end=" ")
    inOrder(root.right)
        
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
 
# Print inorder traversal of the input tree
    print("Inorder traversal of the constructed tree is")
    inOrder(root)
#  invert the tree
    invertTree(root)
#  Print inorder traversal of the mirror tree 
    print("\nInorder traversal of the inverted tree is ")
    inOrder(root)


