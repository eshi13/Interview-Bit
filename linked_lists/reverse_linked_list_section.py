# func: reverse a linked list from position m to n
# @param head: head node of the list
# @param m: starting position m
# @param n: ending position n
# @return: new head node
def reverse_between(head, m, n):
    root = ListNode(0)
    root.next = head
    #Find position m
    prev = root
    count = 1
    while count < m:
        prev = prev.next
        count += 1
    start = prev
    end = prev.next
 
    #Start reversing
    prev = prev.next
    curr = prev.next
    while count < n:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1
 
    start.next = prev
    end.next = curr
 
    return root.next