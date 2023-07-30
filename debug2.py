from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: 'Optional[Node]'):
    oldToCopy = {None: None}

    curr = head
    while curr:
        copy = Node(curr.val)
        oldToCopy[curr] = copy
        curr = curr.next

    curr = head
    while curr:
        copy = oldToCopy[curr]
        copy.next = oldToCopy[curr.next]
        copy.random = oldToCopy[curr.random]
        curr = curr.next

    return oldToCopy[head]

print(copyRandomList(head = [[7,None],[13,0],[11,4],[10,2],[1,0]]))