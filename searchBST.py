class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root.val == val:
            return root
        if root.val>val:
            if root.left:
                return self.searchBST(root.left,val)
            else:
                return None
        else:
            if root.right:
                return self.searchBST(root.right,val)
            else:
                return None