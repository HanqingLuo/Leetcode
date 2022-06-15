# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.isSameTree(root, subRoot): return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        

    # 100. 相同的树
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: 
            return True
        if p and q and p.val == q.val: 
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        return False