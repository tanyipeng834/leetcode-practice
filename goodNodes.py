# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.traversal(root,root.val)
        


    def traversal(self,root,max):
        count =0

        if root!= None:
            if root.val >=max:
                count +=1
                max = root.val
            count += self.traversal(root.right,max)
            count += self.traversal(root.left,max)
        return count
        
            