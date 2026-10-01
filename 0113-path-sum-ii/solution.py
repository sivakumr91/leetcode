# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """

        result = []
        path = []

        def dfs(node, remaining):
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            # Check if it is a leaf
            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(path[:])

            dfs(node.left, remaining)
            dfs(node.right, remaining)

            # Backtrack
            path.pop()

        dfs(root, targetSum)

        return result