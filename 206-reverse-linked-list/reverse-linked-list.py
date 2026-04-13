# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            #first grab the next
            next = curr.next
            #reverse the pointer
            curr.next = prev
            #now move the prev forward to process the next
            prev = curr
            #and curr forward to porcess the next
            curr = next
        #finally once done just return prev
        return prev

        '''
        U - Given a head of a singly linked list i need to reverse the linked list in place
            if no head return [] or Null
        M - trverse throgh the linked list and rewire each pointer
        p - inorder to do this i will have prev, curr, and next as pointers to keep track
            firsit i will set prev to null so it won't point to anything 
            curr will be set to the head 
            while curr:
                #first i will set up the curr.next becuase i am both to break the linking pointers 
                #so inorder not to lose it i will keep track of it using next = curr.next
                then i will reverse the pointer by making curr.next = prev so now curr is pointing to prev
                now i will move prev to curr and curr to next that way i can keep ding this untol there is no more curr
                meaning i have fully reversed the linked lists pointers and finally prev will be at the tail of orginal
                or head of new that way i can return prev
                in case there is no head retirning prev will take care of that age case becuase insitally prev is null
        E - Time = O(N) Space = O(1)
        '''

        