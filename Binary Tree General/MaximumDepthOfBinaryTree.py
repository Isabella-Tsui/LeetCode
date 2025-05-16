# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MaximumDepthOfBinaryTree:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        # since the rec helper is a method in the class it needs to be accessed through self
        # if we had defined it outside, we wouldn't have had to do this
        return self.maxDepthRec(root)

    def maxDepthRec(self, curr: Optional[TreeNode]) -> int:
        # base case
        if curr == None:
            return 0

        # additional work
        left = self.maxDepthRec(curr.left)
        right = self.maxDepthRec(curr.right)

        # recursive call
        return 1 + max(left, right)
