# https://leetcode.com/problems/intersection-of-two-linked-lists/
# T: O(m + n)
# S: O(1)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        p, q = headA, headB
        while p != q:
            if not p:
                p = headB
            else:
                p = p.next
                
            if not q:
                q = headA
            else:
                q = q.next
                
        return p