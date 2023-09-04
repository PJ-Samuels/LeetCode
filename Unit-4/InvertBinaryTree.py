class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

def build_tree_from_array(arr, index=0):
    if index >= len(arr) or arr[index] is None:
        return None
    
    root = TreeNode(arr[index])
    root.left = build_tree_from_array(arr, 2 * index + 1)
    root.right = build_tree_from_array(arr, 2 * index + 2)
    return root

def preorder_traversal(node):
    if not node:
        return []
    return [node.val] + preorder_traversal(node.left) + preorder_traversal(node.right)

def main():
    input_array = [4, 2, 7, 1, 3, 6, 9]
    expected_output = [4, 7, 2, 9, 6, 3, 1]
    root = build_tree_from_array(input_array)
    solution = Solution()
    inverted_root = solution.invertTree(root)
    inverted_values = preorder_traversal(inverted_root)

    print("Expected Output:", expected_output)
    print("Actual Output:", inverted_values)
main()
