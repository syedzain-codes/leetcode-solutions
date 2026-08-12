# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans=[]
        if not root:
            return []
        q=deque([root])
        while q:
            size=len(q)
            level=[]
            for i in range(size):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        for i in range(0,len(ans)):
            if i%2!=0:
                left=0
                right=len(ans[i])-1
                while(left<right):
                    ans[i][left],ans[i][right]=ans[i][right],ans[i][left]

                    left+=1
                    right-=1
        return ans
            
        
 


        
                
        