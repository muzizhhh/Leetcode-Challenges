#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Solution2*. Recursion 
"""
from locale import currency


class Solution(object):      # O(N), o(N)
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, pre = head, None
        def reverse(pre, cur):
            if not cur:
                return pre
            tail = reverse(cur, cur.next)
            cur.next = pre
            return tail
        return reverse(pre, cur)

# @lc code=end
 
    # None 1 -> 2 -> 3 -> 4 -> 5 -> None
    # pre  cur                  
    #      pre  cur
    #                          pre   cur
    #                          tail*  

    # None <-1 <- 2 <- 3 <- 4 <- 5 <- None
