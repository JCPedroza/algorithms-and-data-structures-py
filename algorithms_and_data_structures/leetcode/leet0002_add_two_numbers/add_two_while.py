from typing import Optional as Option
from . import list_node

Node = list_node.ListNode


def add_linklists(anode: Option[Node], bnode: Option[Node]) -> Option[Node]:
    """Add two linked lists that represent digits in a number.
    Uses a while loop.
    Complexity: time O(n), space O(n).
    :param anode: First node of a linked list.
    :param bnode: First node of a linked list.
    :return: Sum of the two linked lists as a linked list.
    """

    acurrent = anode
    bcurrent = bnode
    buffer = Node(0)
    result = buffer
    carry = 0

    while acurrent or bcurrent or carry:
        aval = acurrent.val if acurrent else 0
        bval = bcurrent.val if bcurrent else 0
        acurrent = acurrent.nxt if acurrent else None
        bcurrent = bcurrent.nxt if bcurrent else None

        total = aval + bval + carry
        carry = total // 10
        node = Node(total % 10)
        result.nxt = node
        result = result.nxt

    return buffer.nxt


solution = add_linklists
name = "while loop"
