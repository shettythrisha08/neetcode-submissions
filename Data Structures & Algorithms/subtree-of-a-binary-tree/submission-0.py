# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def same(self,root:Optional[TreeNode],subRoot:Optional[TreeNode]) -> bool:
        if root  is None and subRoot is None:
            return True

        if root is None or subRoot is None :
            return False
            
        if root.val!=subRoot.val:
            return False
        return self.same(root.left,subRoot.left) and self.same(root.right,subRoot.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is not None:
            return False
        if subRoot is None:
            return True
        if root.val==subRoot.val:
           return self.same(root,subRoot) or self.isSubtree(root.right,subRoot)or self.isSubtree(root.left,subRoot)
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)

