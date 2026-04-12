# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2 
        sortedList = ListNode()
        curr = sortedList
        while p1 and p2:
            if p1.val <= p2.val:
                #then add p1 
                curr.next = p1
                #then move the curr to next so that we can add the next one
                curr = curr.next
                p1 = p1.next
            else:
                curr.next = p2
                curr = curr.next
                p2 = p2.next
        #But inside the loop, I was moving p1 and p2, not list1 and list2.
        #So by the time the loop ends, you should attach the leftover using:
        if p1:
            curr.next = p1
        else:
            curr.next = p2
        #return the dummynode.next
        return sortedList.next
        '''
        Given the had heads of two sorted linked list merge the two lists, the list should be made by splicin 
        so maybe use a two pointer that way compare the node 1 of list 1 with node 1 in list2 and then comapre 
        if p1 <= p2 just take p1 else take p2 curr.next = p2, if am done with list1 then just add the whole l2 else l1

        M - Two pointers
        P - initalize two pointer p1 and p2 p1 = list1 p2 = list2
            sortedList = ListNode()
            curr = sortedList
            The while p1 and p2:
                if p1.val <= p2.val
                    #then add p1 
                    curr.next = p1
                    #then move the curr to next so that we can add the next one
                    curr = curr.next
                else:
                    curr.next = p2
                    curr = curr.next
            if not list1:
                curr.next = list2
            else:
                sortedList.next = list1
            return sortedList

        '''