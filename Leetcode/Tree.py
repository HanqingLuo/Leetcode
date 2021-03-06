# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 二叉树前序遍历 (Leetcode 144)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:   
        if not root:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
    # 二叉树中序遍历 (Leetcode 94)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:   
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
    # 二叉树后序遍历 (Leetcode 145)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:   
        if not root:
            return []
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    # 相同的二叉树 (Leetcode 100)
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: 
            return True
        if p and q and p.val == q.val: 
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        return False

    # 104. 二叉树的最大深度
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    # 226. 翻转二叉树
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        root.left, root.right = root.right, root.left # 在本节点的操作，左右孩子互换
        # 已经搞定的左右孩子，使用递归的思路写出函数表达式。下面两句的顺序并不重要
        self.invertTree(root.right) 
        self.invertTree(root.left)
        return root

    # 102. 二叉树的层序遍历
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        q = collections.deque()
        q.append(root)

        while q: # run BFS while q is not empty
            qLen = len(q) 
            level = [] 
            for i in range(qLen):
                node = q.popleft()
                if node: # node could be None
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level: # we dont wanna None level
                ans.append(level)
        return ans

    # 98. 验证二叉搜索树
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            if not node: return True
            if node and node.val >= high or node.val <= low:return False
            return validate(node.left,low,node.val) and validate(node.right,node.val,high)
        return validate(root)
            

    # 235. 二叉搜索树的最近公共祖先
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while True:
            if p.val > node.val and q.val > node.val:
                node = node.right
            elif p.val < node.val and q.val < node.val:
                node = node.left
            else: 
                return node
    # 572. Subtree of Another Tree
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.isSameTree(root, subRoot): return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
            
            
            
        


    