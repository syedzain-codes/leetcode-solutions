# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans=[]
        def dfs(root):
            if root is None:
                return
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        ans.sort()
        mind=ans[len(ans)-1]
        for i in range(0,len(ans)):
            for j in range(i+1,len(ans)):
                mind=min(mind,ans[j]-ans[i])
        return mind


        