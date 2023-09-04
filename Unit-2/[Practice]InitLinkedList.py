class ListNode:
    def _init_(self, val):
        val = self.val
        val.next = None
    def insert(self, val):
        n = ListNode(val)
        n.next = self
        return n

def main():
    head = ListNode(1)
    print( head)


