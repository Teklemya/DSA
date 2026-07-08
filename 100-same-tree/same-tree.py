# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        leftSubtree = self.isSameTree(p.left, q.left)
        rightSubtree = self.isSameTree(p.right, q.right)

        return (leftSubtree and rightSubtree) | False



        '''
        Given a roots of two binary trees we are expected to check if they are structrally identical and also each node has the same val
        Return a boolean True / False
        M - Recusrsion
        P - 
            Base case:
                if not p and if not q:
                    return True
                if not p or if not q:
                    return False
                if p.val != q.val:
                    return False 
            #recurance equation
                leftSub = isSameTree(p.left, q.left)
                rightSub = isSameTree(p.right, q.right)
            leftSub and rightSub:
                return True
            else:
                False
            return leftSub and rightSub || 
                
        '''