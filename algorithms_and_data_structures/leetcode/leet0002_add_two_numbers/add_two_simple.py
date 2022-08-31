from typing import Optional
from . import list_node

ListNode = list_node.ListNode


def add_linklists(
    anode: Optional[ListNode],
    bnode: Optional[ListNode],
) -> Optional[ListNode]:
    """Add two linked lists that represent digits in a number.
    Uses simple recursion.
    Complexity: time O(n), space O(n).
    :param anode: First node of a linked list.
    :param bnode: First node of a linked list.
    :return: Sum of the two linked lists as a linked list.
    """

    def loop(xnode, ynode, carry=0):
        if xnode or ynode or carry:
            xval = xnode.val if xnode else 0
            yval = ynode.val if ynode else 0

            total = xval + yval + carry
            digit = total % 10
            nxt_carry = total // 10

            xnxt = xnode.nxt if xnode else None
            ynxt = ynode.nxt if ynode else None
            return ListNode(digit, loop(xnxt, ynxt, nxt_carry))

        return None

    return loop(anode, bnode)


solution = add_linklists
name = "simple recursion"
