# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root: return None

        # 在本节点的操作，左右孩子互换
        root.left, root.right = root.right, root.left

        # 已经搞定的左右孩子，使用递归的思路写出函数表达式  
        self.invertTree(root.right) # 下面两句的顺序并不重要
        self.invertTree(root.left)
        return root