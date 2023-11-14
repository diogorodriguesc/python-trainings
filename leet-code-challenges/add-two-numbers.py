# https://leetcode.com/problems/add-two-numbers
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        a = list()
        currentNode = self
        while (currentNode):
            a.append(currentNode.val)
            currentNode = currentNode.next
        
        return "Values: %s" % (a)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        transition = 0
        total_list_node = total_list_node_root = ListNode()

        while(l1 or l2):
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0

            total = l1_val + l2_val + transition
            transition = 1 if total > 9 else 0
            total_list_node.val = total%10

            if (l1):
                l1 = l1.next
            if (l2):    
                l2 = l2.next

            if (l1 or l2):
                total_list_node.next = total_list_node = ListNode(transition)

        if transition > 0:
            total_list_node.next = total_list_node = ListNode(transition)

        return total_list_node_root
    
solution = Solution()

print([solution.addTwoNumbers(ListNode(9, ListNode(2, ListNode(3))),ListNode(9, ListNode(1)))])
print([solution.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9))),ListNode(9, ListNode(9, ListNode(9))))])