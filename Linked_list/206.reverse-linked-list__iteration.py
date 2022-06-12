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
Solution 1: Ieration with fast and slow pointers (and temp pointer)

首先定义一个cur指针，指向头结点，再定义一个pre指针，初始化为null。
然后就要开始反转了，首先要把 cur->next 节点用tmp指针保存一下，也就是保存一下这个节点。
为什么要保存一下这个节点呢，因为接下来要改变 cur->next 的指向了，将cur->next 指向pre ，此时已经反转了第一个节点了。
接下来，就是循环走如下代码逻辑了，继续移动pre和cur指针。
最后，cur 指针已经指向了null，循环结束，链表也反转完毕了。 此时我们return pre指针就可以了，pre指针就指向了新的头结点。
Ref:
1. https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0206.%E7%BF%BB%E8%BD%AC%E9%93%BE%E8%A1%A8.md
"""
class Solution(object):     # O(n) and O(1)
    def reverseList(self, head):
        fast = head   
        slow = None
        while fast:
            temp = fast.next # save the next pointer of fast pointer--> temp will change to fast pointer
            fast.next = slow # the arrow changes direction 
            #update fast and slow pointer
            slow = fast
            fast = temp
        return slow
        
# @lc code=end

"""
O（n) & O(1)
"""