class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def solution(val, count):
    if not val:
        return count
    left_depth = solution( val.left, count+1)
    right_depth = solution(val.right, count+1)
    return max(left_depth, right_depth)


def main():
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    res = solution(head, 0)
    print(res)
main()
    