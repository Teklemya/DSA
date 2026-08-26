# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        #now search 
        #if key greater then we need to go into right subtree, vice versa
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        #we found the node we want to delete
        else:
            #does it have a child? only 1
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            #we can either deicde to go left and find the max val (right) or go right and find min val(left)
            curr = root.right
            #we want to make sure curr has a value and not null
            while curr.left:
                curr = curr.left
            #once we found the minumum then we can assign the value to the root
            root.val = curr.val
            #since we have duplicates we need to delete it
            root.right = self.deleteNode(root.right, curr.val)
        return root


        '''
        We are given a root for the BST and a int - key, if the node.val == key; delete and return
        possibly updated root node or just the same BST 
        Edge case: all are unqiue 
        Empty -> Empty 
        [5], key = 5 -> None

        def searchNode(self, root, key)
        if not root:
            return root
        if key < root.val:
            return searchNode(root.left, key)
        elif key > root.val:
            return searchNode(root.right, key)
        else:
            #we found the node
            return root

        case 1:



        '''