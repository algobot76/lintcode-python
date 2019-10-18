"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        _, subtree, _ = self.helper(root)
        return subtree

    def helper(self, root):
        if root is None:
            return sys.maxsize, None, 0

        left_min, left_subtree, left_sum = self.helper(root.left)
        right_min, right_subtree, right_sum = self.helper(root.right)

        sum_ = left_sum + right_sum + root.val
        if left_min == min(left_min, right_min, sum_):
            return left_min, left_subtree, sum_
        if right_min == min(left_min, right_min, sum_):
            return right_min, right_subtree, sum_

        return sum_, root, sum_
