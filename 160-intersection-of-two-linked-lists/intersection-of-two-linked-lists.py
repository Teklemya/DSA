# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB

        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1












######################################## Brute Force #################################
        # seen = set()

        # while p1:
        #     #add the node to seen 
        #     seen.add(p1) 
        #     #once added move it
        #     p1 = p1.next
        
        # while p2:
        #     #if this node is in seen then i have reached the intersection point
        #     if p2 in seen:
        #         return p2
        #     else:
        #         #move the pointer 2
        #         p2 = p2.next
        # return None
#time = O(m + n)
#space = O(m) m is list 1 n is list 2

'''
I am given two linkedList with an intersection spot and i am supposed to find that and return the value of that node
however if this two do not meet i will have to return a null

M - I will use a set and maybe start with p1 and p2 at headA and headB
P - Once i have my pointer i will move pointer one to the end to keep track of the node and add it to the set
    then i will move p2 and check if Node exisits in seen: if so return the node if not return None
'''