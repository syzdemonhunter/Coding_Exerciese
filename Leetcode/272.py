# https://leetcode.com/problems/closest-binary-search-tree-value-ii/
# T: O(n)
# S: O(n)
# Inorder

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        inorder = self.inorder_traversal(root)
        result = inorder[:k]
        for i in range(k, len(inorder)):
            if abs(result[0] - target) > abs(inorder[i] - target):
                result.append(inorder[i])
                result = result[1:]
            else:
                return result
        return result


    def inorder_traversal(self,root):
        stack=[]
        res=[]
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                res.append(root.val)
                root=root.right
        return res
        