# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
# 有樹的資料，要求任意兩節點的最長直徑

# 樹
from typing import Optional #Optional其實就是聯集,可以有可以沒有

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 資料這樣塞進樹的
# root = TreeNode(0)
# root.left = TreeNode(1)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 設定起始值 = 0
        self.diameter = 0
        
        # 计算每个节点的高度，同时更新直径
        def depth(node: TreeNode) -> int:
            if not node:
                return 0
            
            # 遞迴计算當前left和right的深度
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # 用max函式來讓深度與當前最大深度做比較
            self.diameter = max(self.diameter, left_depth + right_depth)

            # 返回当前节点的深度
            return max(left_depth, right_depth) + 1
        
        # 启动递归
        depth(root)
        
        return self.diameter

