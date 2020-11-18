'''
Check if a linked list is a palindrome using string
'''
def is_palindrome_string(head):
    curr = head
    s = ""
    while head:
        s += str(curr.data)
        curr = curr.next
    return s == s[::-1]




'''
Check if a linked list is a palindrome using two pointers
'''
def is_palindrome_pointers(head):
    if head:
        p = head
        q = head
        prev = []

        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i - 1]

        count = 1

        while count <= i//2 + 1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True
    else:
        return True
