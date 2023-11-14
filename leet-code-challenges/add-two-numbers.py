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
        total_list_node_root = ListNode()
        total_list_node = total_list_node_root

        while(l1 or l2):
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0

            total = l1_val + l2_val + transition

            transition = 1 if total > 9 else 0

            total = total%10
            total_list_node.val = total

            if (l1 is not None):
                l1 = l1.next
            if (l2 is not None):    
                l2 = l2.next

            if (l1 is not None or l2 is not None):
                new_node = ListNode()
                total_list_node.next = new_node
                total_list_node = new_node

        return total_list_node_root
    
solution = Solution()

print([solution.addTwoNumbers(ListNode(9, ListNode(2, ListNode(3))),ListNode(9, ListNode(1)))])
print([solution.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9))),ListNode(9, ListNode(9, ListNode(9))))])