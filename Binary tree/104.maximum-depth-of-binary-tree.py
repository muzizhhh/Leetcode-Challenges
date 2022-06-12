#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Solution 1: iteration 遍历整棵树
depth记录没分支深度，res记录最大深度.
进入节点之前， depth+1， 出了节点之后，depth-1
O(exponential)
"""
class Solution(object):

    depth = 0
    res = 0
    def maxDepth(self, root):
        self.treverse(root)
        return self.res

    def treverse(self,root):
        # base case
        if not root:
            return root
        self.depth += 1    #前序位置
        if not root.left and not root.right:
            self.res = max(self.depth, self.res)
        
        self.treverse(root.left)
        self.treverse(root.right)
        self.depth -= 1   #后序位置

"""
Solution 2：迭代 （后序遍历,左->右->中）
一棵二叉树的最大深度可以通过子树的最大高度推导出来
subproblem: 看每个节点发生什么，分解为左右子树的最大深度
logic: 左右取最大深度
base case: root为空 返回0
"""
class Solution(object):
    def maxDepth(self, root):
        # base case
        if not root:
            return 0

        left_height = self.maxDepth(root.left) 
        right_height = self.maxDepth(root.right)
        depth = max(left_height, right_height)+1    #高度要加上根节点
        return depth


# @lc code=end

