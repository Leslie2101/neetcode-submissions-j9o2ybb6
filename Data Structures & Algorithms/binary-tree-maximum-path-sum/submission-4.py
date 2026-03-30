# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        


        # recursion relationship
        # max path sum of a current node = max sum of single left + max of single right + cur node 
        # return value of max single to parent max(singleLeft, singleRight) + cur node 


        # return maxSingle, maxOverall 
        def helper(node) -> List[int]:
            if node == None:
                return 0, -math.inf

            singleLeft, overallLeft = helper(node.left)
            singleRight, overallRight = helper(node.right)


            return max(singleLeft, singleRight, 0) + node.val, max(overallLeft, overallRight, max(singleLeft, singleRight, 0, singleLeft + singleRight) + node.val)
        
        return helper(root)[1]
