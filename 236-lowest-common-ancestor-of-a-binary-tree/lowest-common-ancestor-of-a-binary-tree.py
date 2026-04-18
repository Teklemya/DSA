# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        #dfs(node) returns whether p or q was found in this subtree, and if both are found in different sides or one is the current node, 
        #then this node is the LCA.
        def dfs(node):
            #if Node is none
            if not node:
                return None
            #I found one of the targets here, so I will bubble this node upward.
            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right) 

            if left and right:
                return node
            
            elif left and not right:
                return left
                
            elif not left and right:
                return right

            else:
                return None
        return dfs(root)
            

    '''
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
        
    take 5 and 1, we start at 3 and left will go one deeper and find 5 and return 5 then right will go deep and find 1 which is q 
    so at node 3 we have found both we return the node / 3 that is the LCA

    P = 5 and q = 4

    now still left would get 5 and right would still be going 
    '''

    #case 1
    '''
        if both left and right are not null then that means we have found one in left and one in right subtree
        that means that node is wehre they frist split 
        return node
    '''
    #case 2 
    '''
        If:
            left exists, right is None → return left
            right exists, left is None → return right
    '''

    '''
    I will use a dfs apporach to see if i can find p or q as i travese the tree 
    one base case is if it is not root then return None
    in my dfs i will have a base case to check if i have found p or q in the left or right or if the node it self is one of them
    “Each subtree tells its parent whether it found p, q, or nothing”

    I’ll do a postorder DFS. For each node, I ask my left and right subtrees whether they contain p or q. If both sides return a 
    non-null result, then the current node is the LCA. If only one side returns a node, I pass that result upward. If the current 
    node itself is p or q, I return it.
    '''