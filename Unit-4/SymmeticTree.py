class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
def solution(val):
    if not val:
        return True
    def symCheck(left, right):
        if not left and not right:#base case
            return True
        if left and right and left.val == right.val:#keep checking
            return symCheck(left.left,right.right ) and (left.right, right.left)
        else:
            return False
    left_branch = val.left
    right_branch = val.right
    ans = symCheck(left_branch, right_branch)
    return ans
def main():
    print()
main()