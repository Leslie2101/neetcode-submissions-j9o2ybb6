# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from sortedcontainers import SortedDict
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        # maybe encode with complete bin tree
        res = SortedDict()

        if root == None:
            return ""
            
        queue = deque([(root, 0)])
        while queue:
            node, val = queue.popleft()

            res[val] = node.val 
            
            if node.left != None:
                queue.append((node.left, val*2+1))
            
            if node.right != None:
                queue.append((node.right, val*2+2))

        lst = ["None"]*(max(res.keys())+1)
        for key, val in res.items():
            lst[key] = str(val)

        print(lst)
        return " ".join(lst)





        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        lst = data.split()

        if not lst:
            return None 

        root = TreeNode(val=int(lst[0]))

        nodeLst = [None]*len(lst)
        nodeLst[0] = root 

        for i in range(1, len(lst)):
            print(nodeLst)
            parent = nodeLst[(i-1)//2]
            print(lst[i], (i-1)//2)

            if lst[i].isdigit():
                node = TreeNode(val=int(lst[i]))
                
                if i % 2 == 1:
                    parent.left = node
                else:
                    parent.right = node 
                
                nodeLst[i] = node
        
        return nodeLst[0]




