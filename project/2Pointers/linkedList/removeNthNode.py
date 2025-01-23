from linkedList import LinkedList
from linkedListNode import LinkedListNode


def remove_nth_last_node(head, n):
    # Replace this placeholder return statement with your code
    prev = None
    left = head
    right = left
    for i in range(1, n):
        right = right.next
    if right.next is None:
        return left.next
    while right.next is not None:
        right = right.next
        prev = left
        left = left.next
    prev.next = left.next
    return head





