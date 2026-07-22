# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s, t):
        '''
        If both are null then it would be true
        If both have the same value we need to check the descdenets 
        If Root is null and subtree has value then that would be false
        if root has value and the subtree is null thne that would be true
        '''
        if not t: return True
        if not s: return False
        #if they are the s
        if self.sameTree(s, t):
            return True
        #what if not subtree so comapre t to the left or right subtree
        return (self.isSubtree(s.left, t) or
            self.isSubtree(s.right, t))

        
    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            #check the decendaents
            return (self.sameTree(s.left, t.left) and
                self.sameTree(s.right, t.right))
        return False