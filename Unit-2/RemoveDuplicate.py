from typing import Optional

class ListNode: 
    def __init__(self, val):
        self.val = val
        self.next = None
    def insert(self, val):
        n = ListNode(val)
        n.next = self
        return n
    def list_length(self):
        c = self
        l = 0
        while c:
            l += 1
            c = c.next
        return l
    def delete(self, val):
        s = ListNode("sentinel")
        s.next = self
        p = s
        c = self
        while c:
            if c.val == val:
                p.next = c.next
                return s.next
            p = c
            c = c.next
        return s.next 
def solution(head):
    current = head 
    while(current is not None):
        next = current.next
        while(next is not None and next.val == current.val):
            next = next.next
        current.next = next
        current = next
    return(head)



def main():
    arr = [1, 1, 2, 3, 3]
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)): 
        current.next = ListNode(arr[i])
        current = current.next
    print("Original Linked List:")
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    head = solution(head)
    print()
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
main()