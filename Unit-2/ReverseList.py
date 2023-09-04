class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    def insert(self, val):
        n = ListNode(val)
        n.next = self
        return n
    

def solution(head):
    prev =  None
    curr = head
    while curr is not None:
        next_val = curr.next
        curr.next = prev
        prev = curr
        curr = next_val
    return prev

def main():
    arr = [5,4,3,2,1]
    head = ListNode(arr[0])
    current = head
    for i in range (1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    print(head.val)    
    print(solution(head).val)

main()
