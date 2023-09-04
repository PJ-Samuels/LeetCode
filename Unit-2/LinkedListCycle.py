class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    def insert (self, val):
        n = ListNode(val)
        n.next = self
        return n
    
def solution(head):
    slow = head
    fast = head.next
    try:
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False
    


def main():
    arr = [3,2,0,4]
    current =ListNode(arr[0])
    head = current
    node_with_val2 = None
    for i in range(1, len(arr)): 
        if current.val == 2:
            node_with_val2 = current
        current.next = ListNode(arr[i])
        current = current.next
    print(current.val)
    current.next = node_with_val2
    print(solution(head))
main()