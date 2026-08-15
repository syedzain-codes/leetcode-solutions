# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.x=TreeNode()
        
        
        z=self.x
        
        def dfs(root):
            if root is None:
                return

            left = root.left
            right = root.right

            self.x.right = root
            self.x.left = None
            self.x = self.x.right

            dfs(left)
            dfs(right)

        dfs(root)

        return z.right

        