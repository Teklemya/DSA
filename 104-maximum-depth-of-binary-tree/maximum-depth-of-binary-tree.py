# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        maxDepth = 0
        #set up dfs
        def dfs(node, depth):
            nonlocal maxDepth # Tells Python to use the maxDepth from the outer scope

            if not node:
                return
            # add to the depth since we see a node and the base case is not hit
            depth += 1
            maxDepth = max(maxDepth, depth)
            #call dfs on children and pass in current depth as well
            dfs(node.left, depth)
            dfs(node.right, depth)
        # Actually trigger the DFS traversal
        dfs(root, depth)

        return maxDepth

        