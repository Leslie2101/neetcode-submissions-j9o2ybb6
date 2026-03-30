# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = []

        def dfs(node):
            if node == None:
                res.append("N")
                return 
            
            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        path = data.split(',')

        root = None 
        cur = root 
        
        def dfs(i):
            
            if path[i] == 'N':
                return None, i 
            
            node = TreeNode(val=int(path[i]))

            lftNode, lftEnd = dfs(i+1)

            rgtNode, rgtEnd = dfs(lftEnd+1)
            node.left = lftNode
            node.right = rgtNode


            return node, rgtEnd
        
        return dfs(0)[0]
