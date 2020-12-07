def is_circular_linked_list(head):
    """
    Determine if a linked list is a circular linked list.
    """
    curr = head
    if not curr:
        return False
    while curr.next != head:
        curr = curr.next
        if not curr:
            return False
    return True