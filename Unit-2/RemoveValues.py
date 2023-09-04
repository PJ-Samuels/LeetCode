class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def insert(self, val):
        n = ListNode(val)
        n.next = self
        return n
    

def solution(head, val):
    curr = head
    prev = None
    while curr is not None:
        
        if curr.val == val:
            prev.next = curr.next
        curr = curr.next 
        prev = curr
    return head
def main():
    arr = [1,2,6,3,4,5,6]
    head = ListNode(arr[0])
    curr = head

    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    
    newhead = solution(head, 6)
    while(newhead):
        print(newhead.val)
        newhead = newhead.next
main()