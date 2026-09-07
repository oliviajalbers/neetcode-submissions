# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        myArray = []
        while (head):
            myArray.append(head.val)
            head = head.next
        i = len(myArray) - 1
        newHead = None
        if (i >= 0):
            newHead = ListNode(myArray[i])
            current = newHead
            while i > 0:
                i -= 1
                newNode = ListNode(myArray[i])   
                current.next = newNode
                current = current.next
        return newHead     