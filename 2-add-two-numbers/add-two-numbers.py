# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and l2:
            return None

        addedList = ListNode()
        curr = addedList
        p1, p2 = l1, l2
        currSum = 0
        reminder = 0
        carry = 0

        while p1 and p2:
            #the reason i added reminder here is i want to carry over any reminder to the next calculation
            currSum = p1.val + p2.val + carry
            #if the currSum is greater than 10 then there is a carry so update that
            if currSum >= 10:
                reminder = currSum % 10
                carry = currSum // 10
                #Then the reminder will be added on the new addedList
                curr.next = ListNode(reminder)
                curr = curr.next
            else:
                carry = 0
            #now if the currSum < 10  add the currSum as a node into the new linked list and move curr
                curr.next = ListNode(currSum)
                curr = curr.next
            #finally move the two pointers
            p1 = p1.next
            p2 = p2.next

        #if only p1 exists there are 3 cases, both None, only P1 or Only p2
        while p1:
            currSum = p1.val + carry
            if currSum >= 10:
                reminder = currSum % 10
                carry = currSum // 10
                #Then the reminder will be added on the new addedList
                curr.next = ListNode(reminder)
                curr = curr.next
            else:
                carry = 0
            #now if the currSum < 10  add the currSum as a node into the new linked list and move curr
                curr.next = ListNode(currSum)
                curr = curr.next
            p1 = p1.next
        while p2:
            currSum = p2.val + carry
            if currSum >= 10:
                reminder = currSum % 10
                carry = currSum // 10
                #Then the reminder will be added on the new addedList
                curr.next = ListNode(reminder)
                curr = curr.next
            else:
                carry = 0
            #now if the currSum < 10  add the currSum as a node into the new linked list and move curr
                curr.next = ListNode(currSum)
                curr = curr.next
            p2 = p2.next

        #for the final carry, i will just add it last
        if carry > 0:
            curr.next = ListNode(carry)
            curr = curr.next

        return addedList.next



'''
Give two linked list add the nodes and return the sum as a linked list
inorder to do this i need a new linked list and two pointers to keep track

if both p1 and p2
then as i add if currSum = p1 + p2 + reminder > 10 then i will get the reminder which will be
reminder = currSum % 10 which i will keep adding into the next currSun
I will then do curr = addedList and then curr.next = ListNode(currSum) and the move curr = curr.next
i will then move p1 and p2 to next

if only p1 then:
    addList.next = p1
    if reminder > 0
    addList.next = ListNode(reminder)
else:
    ...
return addList.next
'''