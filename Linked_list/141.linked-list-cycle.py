class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Fast and slow pointers,faster goes with two steps and slow pointer goes with one step. 
        Once they meet at the same node, has cycle 
        O(N) & O(1)
        """
        # initiate two pointers to head
        p1, p2 = head,head  
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                return True
        return False
        
# @lc code=end

