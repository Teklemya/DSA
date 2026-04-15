# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        #using a set to check if visted or not   
        # seen = set()
        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next
        # return False



        # slow = head
        # fast = head

        # while fast != None and fast.next != None:
        #     slow = slow.next      # 2, 0, -4
        #     fast = fast.next.next # 0, 2, -4
        #     if fast == slow:
        #         return True
        # return False 
        
        '''
        Understand - > A linked list is said to have a cycle if some node can be
         reached again as we follow the pointer (reference)
         Edge case - single node
        M - Two pointer
        P - we can set the slow and fast pointer to head, then iterate through
        the Linked List and if the fast pointer reaches the slow pointer then we
        return true else False
        Time - O(n) for all the transveral
        Space - O(1)
        '''
        