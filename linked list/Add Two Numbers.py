# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)

        currentNode = dummy
        extra = 0
        while l1 or l2:
            currentSum = extra
            if l1:
                currentSum += l1.val
                l1 = l1.next
            if l2:
                currentSum += l2.val
                l2 = l2.next

            currentNode.next = ListNode(currentSum % 10)
            currentNode = currentNode.next
            extra = currentSum // 10
        if extra > 0:
            currentNode.next = ListNode(extra)

        return dummy.next