from typing import Optional
from . import list_node

ListNode = list_node.ListNode


def add_linklists(
    anode: Optional[ListNode],
    bnode: Optional[ListNode],
) -> Optional[ListNode]:
    """Add two linked lists that represent digits in a number.
    :param anode: First node of a linked list.
    :param bnode: First node of a linked list.
    :return: Sum of the two linked lists as a linked list.
    """

    acurrent = anode
    bcurrent = bnode
    dummy_head = ListNode(0)
    outcurrent = dummy_head
    carry = 0

    while acurrent or bcurrent or carry:
        aval = acurrent.val if acurrent else 0
        bval = bcurrent.val if bcurrent else 0

        total = aval + bval + carry
        digit = total % 10
        carry = total // 10
        node = ListNode(digit)
        outcurrent.nxt = node
        outcurrent = outcurrent.nxt

        acurrent = acurrent.nxt if acurrent else None
        bcurrent = bcurrent.nxt if bcurrent else None

    return dummy_head.nxt


solution = add_linklists
name = "while loop"
